from app.scraper import CurrencyScraper
from app.bot.main import main as bot_main
from app.scheduler import start_scheduler

async def main():
    currency_scrapey = CurrencyScraper()
    currency_scrapey()
    start_scheduler()
    await bot_main()


if __name__ == "__main__":
    import asyncio
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Program interrupted by user.")