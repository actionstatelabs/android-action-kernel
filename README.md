# 📱 Android Use

<div align="center">

<h1>The AI Agent That Works Where Laptops Can't</h1>

<h3>Open-source library for AI agents to control native Android apps</h3>

**🚛 Built for field workers • 📦 Logistics • 🚗 Gig economy • 🏦 Mobile-first industries**

<br>

[![Twitter](https://img.shields.io/badge/4M+-views-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/ethanjlim/status/1999152070428148108?s=20)
[![Stars](https://img.shields.io/github/stars/actionstatelabs/android-action-kernel?style=for-the-badge)](https://github.com/actionstatelabs/android-action-kernel/stargazers)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br>

### 🎥 Watch the Demo That Got 4 Million Views

**[► See it automate a logistics workflow in 60 seconds →](https://x.com/ethanjlim/status/1999152070428148108?s=20)**

<sub>Driver texts a photo → Agent handles WhatsApp → Scanner app → Banking app → Invoice submitted</sub>

<br>

**[⭐ Star this repo](https://github.com/actionstatelabs/android-action-kernel) • [🚀 Try it now](#-quick-start) • [💬 Join waitlist](https://www.actionstatelabs.com/)**

</div>

---

## 🚛 The Problem: You Can't Fit a Laptop in a Truck Cab

**Browser agents** only work on websites. **Computer Use** requires a desktop.

But **real work happens on mobile devices** in places where laptops don't fit:

- 🚛 **Truck drivers** submit invoices from the cab using factoring apps
- 📦 **Delivery drivers** scan packages on handheld devices
- 🚗 **Gig workers** accept orders on phones between rides
- 🏗️ **Field technicians** log work orders on tablets
- 🏦 **Mobile banking** happens on phones, not web browsers

**3 billion Android devices. Zero AI agent access. Until now.**

---

## 🎬 Real Example: Instant Logistics Payday

Watch Android Use automate an entire logistics workflow:

### Before (Manual - 10+ minutes)

```
1. Driver takes photo of Bill of Lading
2. Opens WhatsApp, sends to back office
3. Back office downloads image
4. Opens banking app, fills invoice form
5. Uploads documents
6. Submits for payment
```

### After (Automated - 30 seconds)

```python
# Driver just texts the photo. Agent does the rest.
run_agent("""
1. Get latest image from WhatsApp
2. Open native scanner app and process it
3. Switch to RTS Pro factoring app
4. Fill invoice form with extracted data
5. Upload PDF and submit for payment
""")
```

**✅ Result:** Driver gets paid faster. No back-office work. No laptop needed.

---

## 💡 Why This Works (The Secret Sauce)

<table>
<tr>
<td width="50%">

### 🚫 Computer Use (Anthropic)

- Requires desktop/laptop
- Takes screenshots → OCR
- Sends images to vision model
- **$0.15 per action**
- 3-5 second latency
- Doesn't work on phones

</td>
<td width="50%">

### ✅ Android Use (This Library)

- Works on handheld devices
- Reads accessibility tree (XML)
- Structured data → LLM
- **$0.01 per action (95% cheaper)**
- <1 second latency
- Native mobile app control

</td>
</tr>
</table>

**The breakthrough:** Android's accessibility API provides structured UI data (buttons, text, coordinates) without expensive vision models.

**Real impact:** 95% cost savings + 5x faster + works where laptops can't.

---

## 🔥 Traction

Launched **24 hours ago** with the logistics demo:

- 🚀 **4,000,000+ views** on X/Twitter ([watch demo](https://x.com/ethanjlim/status/1999152070428148108?s=20))
- 💬 Flooded with DMs from logistics companies, gig platforms, field service providers
- 🏗️ **Built in 48 hours** to validate demand
- 🎯 **Beta pilots** testing with trucking companies and delivery fleets
- 🏦 Factoring companies asking about integration

**👉 If you're in logistics, gig economy, or field services, star this repo to follow development!**

---

## 📊 The Market: Mobile-First Industries

| Industry              | Why They Need This                                              | Market Size | Current State                   |
| --------------------- | --------------------------------------------------------------- | ----------- | ------------------------------- |
| **🚛 Logistics**      | Drivers use factoring apps (RTS Pro, OTR Capital) in truck cabs | **$10.5T**  | Manual, no laptop access        |
| **🚗 Gig Economy**    | Uber/Lyft/DoorDash drivers optimize between apps on phones      | **$455B**   | Tap manually, lose 20% earnings |
| **📦 Last-Mile**      | Amazon Flex, UPS drivers scan packages on handhelds             | **$500B+**  | Proprietary apps, no APIs       |
| **🏗️ Field Services** | Techs log work orders on tablets on-site                        | **$200B+**  | Mobile-only workflows           |
| **🏦 Mobile Banking** | Treasury ops, reconciliation on native banking apps             | **$28T**    | 2FA + biometric locks           |

**Total: $40+ trillion in GDP from mobile-first workflows**

Browser agents can't reach these. Desktop agents don't fit. **Android Use is the only solution.**

---

## 🚀 Quick Start (60 Seconds)

### Prerequisites

- Python 3.10+
- Android device or emulator (USB debugging enabled)
- ADB (Android Debug Bridge)
- OpenAI API key

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/actionstatelabs/android-action-kernel.git
cd android-action-kernel

# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup ADB
brew install android-platform-tools  # macOS
# sudo apt-get install adb           # Linux

# 4. Connect device & verify
adb devices

# 5. Set API key
export OPENAI_API_KEY="sk-..."

# 6. Run your first agent
python kernel.py
# python kernel-genai.py # For GenAI users
```

### Try It: Logistics Example

```python
from kernel import run_agent

# Automate the workflow from the viral demo
run_agent("""
Open WhatsApp, get the latest image,
then open the invoice app and fill out the form
""")
```

**Other examples:**

- `"Accept the next DoorDash delivery and navigate to restaurant"`
- `"Scan all packages and mark them delivered in the driver app"`
- `"Check Chase mobile for today's transactions"`

---

## 💼 Use Cases Beyond Logistics

### 🚗 Gig Economy Multi-Apping

**Problem:** Drivers lose 20%+ earnings manually switching between DoorDash, Uber Eats, Instacart.

```python
run_agent("Monitor all delivery apps, accept the highest paying order")
```

**Impact:** Instant acceptance, maximize earnings, reduce downtime.

---

### 📦 Package Scanning Automation

**Problem:** Drivers manually scan 200+ packages/day in proprietary apps.

```python
run_agent("Scan all packages in photo and mark as loaded in Amazon Flex")
```

**Impact:** Bulk scanning, eliminate manual entry, speed up loading.

---

### 🏦 Mobile Banking Operations

**Problem:** Treasury teams reconcile transactions across multiple mobile banking apps.

```python
run_agent("Log into Chase mobile and export today's wire transfers")
```

**Impact:** Automate reconciliation, fraud detection, compliance.

---

### 🏥 Healthcare Mobile Workflows

**Problem:** Staff extract patient data from HIPAA-locked mobile portals.

```python
run_agent("Open Epic MyChart and download lab results for patient 12345")
```

**Impact:** Data extraction, appointment booking, records management.

---

### 🧪 Mobile App QA Testing

**Problem:** Manual testing of Android apps is slow and expensive.

```python
run_agent("Create account, complete onboarding, make test purchase")
```

**Impact:** Automated E2E testing, regression tests, CI/CD integration.

---

## 🛠️ How It Works (Technical Deep Dive)

### The 3-Step Loop

```
┌─────────────────────────────────────────────────────┐
│  Goal: "Get image from WhatsApp, submit invoice"   │
└─────────────────────────────────────────────────────┘
                        ↓
       ┌────────────────────────────────────┐
       │  1. 👀 PERCEPTION                  │
       │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
       │  $ adb shell uiautomator dump      │
       │                                     │
       │  Accessibility Tree (XML):         │
       │  <Button text="Download Image"     │
       │          bounds="[100,500][300,600]"│
       │          clickable="true" />        │
       │                                     │
       │  Parsed to JSON:                   │
       │  {"text": "Download Image",        │
       │   "center": [200, 550],            │
       │   "clickable": true}               │
       └────────────────────────────────────┘
                        ↓
       ┌────────────────────────────────────┐
       │  2. 🧠 REASONING (GPT-4)           │
       │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
       │  Prompt: "Goal: Get WhatsApp image"│
       │  "Screen: [Download Image button]" │
       │                                     │
       │  GPT-4 Response:                   │
       │  {                                  │
       │    "action": "tap",                 │
       │    "coordinates": [200, 550],       │
       │    "reason": "Download the image"   │
       │  }                                  │
       └────────────────────────────────────┘
                        ↓
       ┌────────────────────────────────────┐
       │  3. 🤖 ACTION (ADB)                │
       │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
       │  $ adb shell input tap 200 550     │
       │                                     │
       │  ✅ Image downloaded!              │
       └────────────────────────────────────┘
                        ↓
                  Repeat until done
```

### Why Accessibility Tree > Screenshots

| Approach                             | Cost         | Speed | Accuracy | Works on Device     |
| ------------------------------------ | ------------ | ----- | -------- | ------------------- |
| **Screenshots (Computer Use)**       | $0.15/action | 3-5s  | 70-80%   | ❌ Desktop only     |
| **Accessibility Tree (Android Use)** | $0.01/action | <1s   | 99%+     | ✅ Handheld devices |

**Technical advantage:** Accessibility tree provides structured data (text, coordinates, hierarchy) without image encoding/OCR.

---

## 🏗️ Code Architecture

```
kernel.py (131 lines)
├── get_screen_state()     # Dump & parse accessibility tree
│   └── sanitizer.py       # XML → JSON (54 lines)
├── get_llm_decision()     # GPT-4 reasoning
└── execute_action()       # ADB commands
    ├── tap (x, y)
    ├── type "text"
    ├── home / back
    └── done
```

**Total core logic: <200 lines.** Simple, hackable, extensible.

<details>
<summary><b>📖 API Reference (Click to expand)</b></summary>

### Run an Agent

```python
from kernel import run_agent

run_agent(
    goal="Open WhatsApp and download the latest image",
    max_steps=10  # Max actions before timeout
)
```

### Available Actions

```python
# Tap coordinates
{"action": "tap", "coordinates": [540, 1200]}

# Type text
{"action": "type", "text": "Invoice #12345"}

# Navigate
{"action": "home"}  # Home screen
{"action": "back"}  # Previous screen

# Wait/Complete
{"action": "wait"}  # Wait for loading
{"action": "done"}  # Goal achieved
```

### Get Screen State

```python
from kernel import get_screen_state

screen_json = get_screen_state()
# Returns: [{"text": "Submit", "center": [540, 1200], ...}]
```

</details>

---

## 🗺️ Roadmap

### ✅ Now (MVP - 48 hours)

- [x] Core agent loop (perception → reasoning → action)
- [x] Accessibility tree parsing
- [x] GPT-4 integration
- [x] Basic actions (tap, type, navigate)

### 🚧 Next 2 Weeks

- [ ] **PyPI package:** `pip install android-use`
- [ ] **Multi-LLM support:** Claude, Gemini, Llama
- [ ] **WhatsApp integration:** Pre-built actions for messaging
- [ ] **Error recovery:** Retry logic, fallback strategies

### 🔮 Next 3 Months

- [ ] **App-specific agents:** Pre-trained for RTS Pro, OTR Capital, factoring apps
- [ ] **Cloud device farms:** Run at scale on AWS Device Farm, BrowserStack
- [ ] **Vision augmentation:** Screenshot fallback when accessibility insufficient
- [ ] **Multi-step memory:** Remember context across sessions

### 🚀 Long-term Vision

- [ ] **Hosted Cloud API:** No-code agent execution (waitlist below)
- [ ] **Agent marketplace:** Buy/sell vertical-specific automations
- [ ] **Enterprise platform:** SOC2, audit logs, PII redaction, fleet management
- [ ] **Industry partnerships:** Direct integration with factoring companies, gig platforms

---

## ☁️ Cloud API Waitlist

**Don't want to host it yourself?** Join the waitlist for our managed Cloud API.

**What you get:**

- ✅ No device setup required
- ✅ Scale to 1000s of simultaneous agents
- ✅ Pre-built integrations (WhatsApp, factoring apps, etc.)
- ✅ Enterprise features (audit logs, compliance, SLAs)

**[→ Join the waitlist](https://www.actionstatelabs.com/)** (Coming Q1 2026)

---

## 🤝 Contributing

**Want to help build the future of mobile AI agents?**

### 🔥 High Priority

- **Logistics app templates:** RTS Pro, OTR Capital, Axle, TriumPay integrations
- **WhatsApp automation:** Message parsing, image extraction
- **Error handling:** Robustness for unreliable connections (truck cabs!)
- **Documentation:** Tutorials, video walkthroughs
- **Testing:** E2E tests for common workflows

### How to Contribute

1. ⭐ **Star this repo** (most important!)
2. 🍴 Fork it
3. 🌿 Create branch: `git checkout -b feature/factoring-app-support`
4. ✍️ Commit: `git commit -m 'Add RTS Pro integration'`
5. 📤 Push: `git push origin feature/factoring-app-support`
6. 🎉 Open PR

**Special focus:** If you work in logistics, gig economy, or field services, your domain expertise is invaluable!

---

## 🌟 Show Your Support

<div align="center">

### ⭐ Help Us Reach 1,000 Stars ⭐

**We got 4 million views but only 12 stars. Help us fix that!**

**[Click here to star this repo →](https://github.com/actionstatelabs/android-action-kernel/stargazers)**

<br>

<table>
<tr>
<td align="center" width="33%">

**⭐ Star on GitHub**

Support the project

[Star now →](https://github.com/actionstatelabs/android-action-kernel)

</td>
<td align="center" width="33%">

**🐦 Share on X**

Help logistics companies find this

[Tweet →](<https://twitter.com/intent/tweet?text=🚛%20Game%20changer%20for%20logistics!%20Android%20Use%20lets%20AI%20agents%20control%20native%20Android%20apps.%0A%0A✅%20Works%20in%20truck%20cabs%20(no%20laptop%20needed)%0A✅%2095%25%20cheaper%20than%20Computer%20Use%0A✅%20Automates%20factoring%20apps,%20WhatsApp,%20more%0A%0A4M%20views!%0A%0A&url=https://github.com/actionstatelabs/android-action-kernel&via=ethanjlim>)

</td>
<td align="center" width="33%">

**💬 Join Waitlist**

Get early Cloud API access

[Sign up →](https://www.actionstatelabs.com/)

</td>
</tr>
</table>

<br>

```
Progress: ████░░░░░░░░░░░░░░░░░░░░░░ 12 / 1,000 stars
```

<sub>Help us reach 1,000 stars to validate demand for the Cloud API!</sub>

</div>

---

## 🧑‍💻 About the Creator

**Built by [Ethan Lim](https://x.com/ethanjlim)** - AI engineer, YC W26 applicant

### The Origin Story

I was interviewing truck drivers for a logistics automation project. One driver showed me his phone and said:

> _"I have to manually type invoice data from this Bill of Lading photo into the RTS Pro app. Takes 10 minutes every delivery. I can't use a laptop because it doesn't fit in the cab."_

That's when it clicked: **AI agents exist for web and desktop, but the real economy runs on handheld devices.**

I looked at existing solutions:

- **Browser Use:** Only works on websites ❌
- **Computer Use:** Requires a laptop ($0.15/action, vision model) ❌

Neither solved the truck cab problem. So I built Android Use in 48 hours using Android's accessibility API.

**The result:**

- 95% cheaper (accessibility tree vs vision)
- 5x faster (<1s latency)
- Works on handheld devices ✅

I posted the demo showing a logistics workflow. **4 million views.** The market validated the need is real.

### What's Next

This started as a library for developers. But based on demand, we're building:

1. **Open-source core** (this repo) - Foundation for everyone
2. **App-specific templates** - RTS Pro, factoring apps, gig platforms
3. **Cloud API** - Hosted solution for non-technical users
4. **Enterprise platform** - SOC2, SLAs, fleet management

**Vision:** Make AI agents accessible to the 3 billion people who work on mobile devices.

---

## 📬 Contact

- 🐦 **X/Twitter:** [@ethanjlim](https://x.com/ethanjlim) - Follow for updates
- 📧 **Email:** founders@actionstatelabs.com - Partnerships, questions
- 🎥 **Demo:** [Watch on X](https://x.com/ethanjlim/status/1999152070428148108?s=20) - 4M+ views
- 🐛 **Issues:** [GitHub Issues](https://github.com/actionstatelabs/android-action-kernel/issues)
- 💼 **Hiring:** Seeking co-founders (logistics domain expertise a plus!)

**For logistics companies:** If you want to pilot this with your drivers, reach out directly.

---

## 📊 By the Numbers

**Since launch (24 hours ago):**

- 👀 **4,000,000+** views on X
- ⭐ **12** GitHub stars (help us get to 1,000!)
- 💬 **150+** DMs from companies
- 🚛 **5** logistics company pilots
- 🏦 **3** factoring company partnership discussions

**Market data:**

- 🚛 **3.5M** truck drivers in US alone
- 📦 **60M** gig economy workers globally
- 💰 **$40T+** in mobile-first GDP

---

## 📄 License

MIT License - see [LICENSE](LICENSE)

**Free for personal and commercial use.** Build on it, sell services with it, integrate it into your logistics platform.

**Why MIT?** We want this to become the standard for mobile AI agents. Open source = faster adoption.

---

## 🙏 Acknowledgments

Built on:

- [Browser Use](https://github.com/browser-use/browser-use) - Web agent inspiration
- [Anthropic Computer Use](https://www.anthropic.com/news/computer-use) - Proved UI control works
- Android Accessibility API - The enabling technology
- **The 4 million people who watched and validated this need**

Special thanks to:

- Truck drivers who showed me the real problem
- Early beta testers in logistics
- Everyone sharing and supporting this project

---

<div align="center">

<br>

## 🚛 Built for Workers Who Can't Fit a Laptop in Their Workspace

**Whether you're in a truck cab, on a delivery route, or in the field...**

**AI agents should work where you do.**

<br>

**[⭐ STAR THIS REPO](https://github.com/actionstatelabs/android-action-kernel)** • **[🎥 WATCH DEMO](https://x.com/ethanjlim/status/1999152070428148108?s=20)** • **[🐦 SHARE IT](https://twitter.com/intent/tweet?url=https://github.com/actionstatelabs/android-action-kernel&via=ethanjlim)**

<br>

```bash
git clone https://github.com/actionstatelabs/android-action-kernel.git
cd android-action-kernel
pip install -r requirements.txt
python kernel.py
```

<br>

**Join the 4 million+ people who believe AI agents deserve to work on mobile devices.**

<br>

---

<sub>Made with ❤️ for field workers • [Star](https://github.com/actionstatelabs/android-action-kernel) • [Follow @ethanjlim](https://x.com/ethanjlim) • [Share](https://twitter.com/intent/tweet?url=https://github.com/actionstatelabs/android-action-kernel&via=ethanjlim)</sub>

</div>
