
# Telegram Horoscope Bot

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://core.telegram.org/bots)

A simple and interactive Telegram bot that provides daily horoscope predictions based on user input. The bot engages users in a conversational flow to request their zodiac sign and desired day (today, tomorrow, yesterday, or a specific date), and returns horoscope data retrieved from a public API.

---

## Features

- Handles `/start` and `/hello` commands with a friendly welcome message.
- Responds to `/horoscope` command to initiate horoscope interaction.
- Asks users to input their zodiac sign.
- Accepts day inputs: `TODAY`, `TOMORROW`, `YESTERDAY`, or specific dates (`YYYY-MM-DD`).
- Fetches horoscope data via an external API and returns the result.
- Echoes any other user message.

---

## Technologies Used

- Python 3.7+
- pyTelegramBotAPI
- python-dotenv
- Horoscope Public API (https://horoscope-app-api.vercel.app)

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/yourusername/telegram-horoscope-bot.git
cd telegram-horoscope-bot
```

### 2. Install Dependencies

Create a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install required packages:

```
pip install -r requirements.txt
```

### 3. Create and Configure `.env` File

Create a `.env` file in the project root and add your Telegram Bot token:

```
BOT_TOKEN=your_telegram_bot_token_here
```

> You can obtain a bot token from BotFather on Telegram.

---

## Running the Bot

Run the bot locally:

```
python bot.py
```

Once running, you can interact with your bot on Telegram by sending commands like `/start` and `/horoscope`.

---

## Usage Guide

1. Start the bot with `/start` or `/hello`.
2. Use `/horoscope` to begin the horoscope flow.
3. The bot will prompt:
   - Your zodiac sign (e.g., Aries, Taurus, etc.)
   - The day you want the horoscope for (`TODAY`, `TOMORROW`, `YESTERDAY`, or a date like `2025-08-04`)
4. The bot will reply with:
   - Horoscope text
   - Your selected sign
   - The date

---

## Example Interaction

```
User: /horoscope
Bot: What's your zodiac sign?
User: Leo
Bot: What day do you want to know? TODAY, TOMORROW, YESTERDAY, or YYYY-MM-DD?
User: TODAY
Bot: Here's your horoscope!
Bot: Horoscope: [prediction text]
     Sign: Leo
     Day: 2025-08-04
```

---

## Project Structure

```
telegram-horoscope-bot/
├── bot.py              # Main Telegram bot logic
├── horoscope.py        # API interaction logic
├── .env                # Bot token stored securely (not committed)
├── requirements.txt    # Python package dependencies
└── README.md           # Project documentation
```

---

## Horoscope API Details

- Base URL: https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily
- Method: GET
- Parameters:
  - sign: One of the zodiac signs
  - day: TODAY, TOMORROW, YESTERDAY, or a YYYY-MM-DD date

**Sample Request:**

```
GET /api/v1/get-horoscope/daily?sign=Leo&day=TODAY
```

**Sample Response:**

```json
{
  "status": "success",
  "data": {
    "sign": "Leo",
    "date": "2025-08-04",
    "horoscope_data": "You may feel an urge to express yourself..."
  }
}
```

---

## Supported Zodiac Signs

- Aries
- Taurus
- Gemini
- Cancer
- Leo
- Virgo
- Libra
- Scorpio
- Sagittarius
- Capricorn
- Aquarius
- Pisces

---

## Troubleshooting

- **Bot not responding?**
  - Check that `.env` contains the correct token.
  - Ensure internet access.
  - Confirm that you started the bot on Telegram.

- **API issues?**
  - Ensure proper zodiac spelling.
  - Validate the date format or use TODAY, TOMORROW, YESTERDAY.

---

## License

This project is purely for learning purposes.
---

## Author

Developed by Sidney.

For suggestions or issues, open a GitHub issue.
