# WomenShield

## Overview
WomenShield is a Python-based AI filter designed to detect absurd or harmful messages in real-time.  
The prototype demonstrates how suspicious content can be flagged and alerts users with desktop notifications, giving them control to reveal or block the message.

This project was built for hackathon presentation purposes, focusing on **user safety, rapid prototyping, and notification-driven experiences**.

---

## Features
-  Detects suspicious keywords (e.g., "kill")
-  Shows Windows desktop notifications
-  Asks user to reveal or block suspicious messages
-  Simple command-line interface for demo
-  Future vision: actionable Yes/No buttons inside notifications

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/WomenShield.git
cd WomenShield
2. Install Python
Make sure you have Python 3.10+ installed.
Check version:

bash
python --version
3. Install dependencies
Install the required library:

bash
pip install winotify
Usage
Run the demo
bash
python women_shield_notify.py
Demo Flow
Type a safe message → Notification shows with Absurdness chance = 0

Type a suspicious message (e.g., "kill") → Notification warns with Absurdness chance = 1

CMD asks if you want to reveal or block the message

Type exit to quit the demo

#####Future Expansion
Multi-device socket chat → extend filtering across devices
Actionable notifications → Yes/No buttons inside toast popups (via Windows Runtime APIs)
Graphical dashboards → visualize safe vs suspicious message statistics
Advanced AI filters → contextual absurdness detection beyond keywords
