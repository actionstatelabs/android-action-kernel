import os
import time
import subprocess
import json
from typing import Dict, Any, List
from google import genai
import sanitizer
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURATION ---
ADB_PATH = "adb"  # Ensure adb is in your PATH
MODEL = "gemini-2.5-flash"  # Or another Gemini model as needed
SCREEN_DUMP_PATH = "/sdcard/window_dump.xml"
LOCAL_DUMP_PATH = "window_dump.xml"


try:
    client = genai.Client()
except Exception as e:
    # Handle case where API key is not set
    print("Error: Failed to initialize Google Gen AI Client.")
    print("Please ensure the GEMINI_API_KEY environment variable is set.")
    exit(1)
# ------------------------------------------------------


def run_adb_command(command: List[str]):
    """Executes a shell command via ADB."""
    str_command = [str(c) for c in command]
    result = subprocess.run([ADB_PATH] + str_command,
                            capture_output=True, text=True)
    if result.stderr and "error" in result.stderr.lower():
        print(f"❌ ADB Error: {result.stderr.strip()}")
    return result.stdout.strip()


def get_screen_state() -> str:
    """Dumps the current UI XML and returns the sanitized JSON string."""
    # 1. Capture XML
    run_adb_command(["shell", "uiautomator", "dump", SCREEN_DUMP_PATH])

    # 2. Pull to local
    pull_result = subprocess.run(
        [ADB_PATH, "pull", SCREEN_DUMP_PATH, LOCAL_DUMP_PATH], capture_output=True, text=True)
    if pull_result.returncode != 0:
        print(f"❌ ADB Pull Error: {pull_result.stderr.strip()}")
        return "Error: Could not pull screen dump."

    # 3. Read & Sanitize
    if not os.path.exists(LOCAL_DUMP_PATH):
        return "Error: Could not capture screen."

    with open(LOCAL_DUMP_PATH, "r", encoding="utf-8") as f:
        xml_content = f.read()

    elements = sanitizer.get_interactive_elements(xml_content)
    return json.dumps(elements, indent=2)


def execute_action(action: Dict[str, Any]):
    """Executes the action decided by the LLM."""
    act_type = action.get("action")

    if act_type == "tap":
        coordinates = action.get("coordinates", [0, 0])
        x, y = coordinates[0], coordinates[1]
        print(f"👉 Tapping: ({x}, {y})")
        run_adb_command(["shell", "input", "tap", str(x), str(y)])

    elif act_type == "type":
        text_to_type = action.get("text")
        adb_text = text_to_type.replace(
            " ", "%s")  # ADB requires %s for spaces
        print(f"⌨️ Typing: {text_to_type}")
        run_adb_command(["shell", "input", "text", adb_text])

    elif act_type == "home":
        print("🏠 Going Home")
        # Corrected KEYWORDS_HOME to KEYCODE_HOME
        run_adb_command(["shell", "input", "keyevent", "KEYWORDS_HOME"])

    elif act_type == "back":
        print("🔙 Going Back")
        # Corrected KEYWORDS_BACK to KEYCODE_BACK
        run_adb_command(["shell", "input", "keyevent", "KEYWORDS_BACK"])

    elif act_type == "wait":
        print("⏳ Waiting...")
        time.sleep(2)

    elif act_type == "done":
        print("✅ Goal Achieved.")
        exit(0)
    else:
        print(f"⚠️ Unknown action type: {act_type}")


def get_llm_decision(goal: str, screen_context: str) -> Dict[str, Any]:
    """Sends screen context to LLM and asks for the next move using Gemini API."""
    system_prompt = """
    You are an Android Driver Agent. Your job is to achieve the user's goal by navigating the UI.
    
    You will receive:
    1. The User's Goal.
    2. A list of interactive UI elements (JSON) with their (x,y) center coordinates.
    
    You must output ONLY a valid JSON object with your next action.
    
    Available Actions:
    - {"action": "tap", "coordinates": [x, y], "reason": "Why you are tapping"}
    - {"action": "type", "text": "Hello World", "reason": "Why you are typing"}
    - {"action": "home", "reason": "Go to home screen"}
    - {"action": "back", "reason": "Go back"}
    - {"action": "wait", "reason": "Wait for loading"}
    - {"action": "done", "reason": "Task complete"}
    
    Example Output:
    {"action": "tap", "coordinates": [540, 1200], "reason": "Clicking the 'Connect' button"}
    """

    full_prompt = (
        f"{system_prompt}\n\n"
        f"GOAL: {goal}\n\n"
        f"SCREEN_CONTEXT:\n{screen_context}"
    )

    response = client.models.generate_content(
        model=MODEL,
        contents=[{"role": "user", "parts": [{"text": full_prompt}]}],
        config={
            "response_mime_type": "application/json",
        }
    )
    return json.loads(response.text)


def run_agent(goal: str, max_steps=10):
    print(f"🚀 Android Use Agent Started. Goal: {goal}")

    for step in range(max_steps):
        print(f"\n--- Step {step + 1} ---")

        # 1. Perception
        print("👀 Scanning Screen...")
        screen_context = get_screen_state()

        if screen_context.startswith("Error"):
            print(f"❌ Aborting: {screen_context}")
            break

        # 2. Reasoning
        print("🧠 Thinking...")
        try:
            decision = get_llm_decision(goal, screen_context)
        except Exception as e:
            print(f"❌ LLM Decision Error: {e}")
            time.sleep(2)
            continue

        print(f"💡 Decision: {decision.get('reason')}")

        # 3. Action
        execute_action(decision)

        # Wait for UI to update
        time.sleep(2)


if __name__ == "__main__":
    # Example Goal: "Open settings and turn on Wi-Fi"
    GOAL = input("Enter your goal: ")
    if not GOAL:
        print("No goal entered. Exiting.")
    else:
        run_agent(GOAL)
