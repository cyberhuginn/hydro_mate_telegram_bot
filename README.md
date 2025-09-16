# Hydro Mate Telegram Bot

**Author:** Saleh Azimidokht (CyberHuginn)   
**Email:** [contact@cyberhuginn.com](mailto:contact@cyberhuginn.com)  
**Website:** [cyberhuginn.com](https://cyberhuginn.com)  
**License:** Free to use  

---

## Overview

Hydro Mate is a simple Telegram bot that helps users track and maintain their daily water intake.  
It provides reminders based on the user's sleep/wake schedule and personal hydration goals. Users can log their water intake easily with one-tap buttons.

---

## Features

- Collects user info: name, sleep/wake hours, daily water goals, frequency.  
- Provides general hydration guidelines based on gender, activity level, or health conditions.  
- Sends scheduled reminders to drink water throughout the day.  
- Inline buttons to log water intake:
  - 🥛 Glass (150ml)  
  - 🍶 Cup (250ml)  
  - ☕ Mug (70ml)  
  - ⏰ "Can't drink now, remind me later"  
- Tracks daily consumption progress (future enhancement: add persistent storage & charts).  

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/cyberhuginn/hydro-mate-bot.git
cd hydro-mate-bot
```
2. Create a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Create a `.env` file in the project root and add your Telegram bot token:
```bash
API_TOKEN=YOUR_TELEGRAM_BOT_TOKEN 
```
---
## Usage

Run the bot:
```bash
python core/main.py
```

- Start the bot in Telegram with `/start`.  
- Follow the prompts to set up your profile.  
- Receive reminders and log water intake using inline buttons.  

---

## Notes

- Currently uses in-memory storage. For persistent tracking, integrate a database (SQLite/PostgreSQL).  
- Scheduling reminders can be enhanced with libraries like `apscheduler` or `Celery`.  
- Designed to be free and public for everyone.  

---

## Contact

If you have any questions or suggestions, contact **CyberHuginn** at [contact@cyberhuginn.com](mailto:contact@cyberhuginn.com).