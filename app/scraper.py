from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException
import logging
import json
from bs4 import BeautifulSoup

class CurrencyScraper:
    def __init__(self):
        self.url = "https://wise.com/gb/currency-converter/currencies/uzs-uzbekistani-som"
        self.options = Options()
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument('--headless=new')

    def create_driver(self):
        driver = Chrome(options=self.options)
        logging.info("Driver created.")
        return driver
    
    def close_driver(self, driver: Chrome):
        driver.close()
        logging.info("Driver closed.")

    def get_page_source(self):
        """Retrieves the HTML page source synchronously for a given self.url."""
        driver = self.create_driver()
        try:
            driver.get(self.url)
            WebDriverWait(driver, 10)
            html = driver.page_source
            return html
        except TimeoutException:
            logging.warning(f"Timeout waiting for page elements at {self.url}")
            return driver.page_source
        except WebDriverException as e:
            logging.error(f"Error fetching page {self.url}: {e}")
            return None
        finally:
           self.close_driver(driver)
    
    def main(self):
        page_source = self.get_page_source()
        soup = BeautifulSoup(page_source, "html.parser")
        table = soup.find("table", attrs={"class": "table table-condensed"})
        if not table:
            logging.error("Table not found on page.")
            return
        table = str(table)
        currency_code = currency_names(table)
        from_uzs = currency_from_uzs(table)
        to_uzs = currency_to_uzs(table)
        data = list(zip(currency_code, from_uzs, to_uzs))
        rates = {code: {"from_uzs": float(from_uzs), "to_uzs": float(to_uzs)} for code, from_uzs, to_uzs in data}

        with open("./data/data.json", "w", encoding="utf-8") as f:
            json.dump(rates, f, indent=4)

    def __call__(self):
        self.main()


def currency_names(table: str) -> list:
    soup = BeautifulSoup(table, "html.parser")
    items = soup.find_all("tr")[0].find_all("span", attrs={"class": "sr-only"})
    rates = [item.get_text().strip() for item in items]
    return rates

def currency_from_uzs(table:str) -> list:
    soup = BeautifulSoup(table, "html.parser")
    items = soup.find_all("tr")[1].find_all("a")
    rates = [item.get_text().strip() for item in items]
    return rates

def currency_to_uzs(table: str) -> list:
    soup = BeautifulSoup(table, "html.parser")
    items = soup.find_all("tr")[2].find_all("a")
    rates = [item.get_text().strip() for item in items]
    return rates
    