from apscheduler.schedulers.background import BackgroundScheduler

from .scraper import CurrencyScraper


scheduler = BackgroundScheduler()
currency_scraper = CurrencyScraper()

def start_scheduler():
    scheduler.add_job(
        currency_scraper, 
        trigger='interval',
        id='currency_scraper',
        hours=2,
        replace_existing=True)
    scheduler.start()