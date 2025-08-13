# Currency Converter Bot

This project is a Telegram bot that provides currency exchange rates by scraping data from a source website.

## 📌 Features
- Fetches live currency data from Wise.com every 2 hours.
- Provides currency exchange rates via Telegram commands.
- Uses **Selenium** for dynamic page rendering and **BeautifulSoup4** for parsing HTML.
- Scheduled data updates using a scheduler.
- Clean project structure for easy maintenance.

## Project Structure
```
app/
├── bot/              # Telegram bot logic
│ ├── handlers/       # Command and message handlers
│ │ ├── currencies.py # Currency-related commands
│ │ ├── start.py      # /start and /help command
│ ├── main.py         # Bot entry point
│ ├── utils.py        # Utility functions
├── config.py         # Configuration variables
├── scheduler.py      # Scheduler for periodic scraping
├── scraper.py        # Selenium + BeautifulSoup scraping logic
data/
├── data.json         # Saved currency data
.env                  # Environment variables
run.py                # Main script to run the project
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/currency-converter-bot.git
cd currency-converter-bot
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set your environment variables (e.g., Telegram bot token). You can use a `.env` file.
```env
BOT_TOKEN=your_telegram_bot_token
```

## Usage

Run the bot and scheduler:
```bash
python run.py
```

## The bot will:
- Start listening for Telegram commands.
- Scrape Wise.com every 2 hours automatically.
- Store results in data/data.json.
- The scraper will run every 2 hours to update the currency rates.

## Dependencies
- Python
- Selenium
- BeautifulSoup4
- Aiogram
- APScheduler (for scheduling scraping tasks)
- JSON for local storage

## License
This project is licensed under the [MIT License](LICENCE).
