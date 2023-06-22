import re
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Scraper:
    def __init__(self, website_name):
        config = configparser.ConfigParser()
        config.read("config.ini")

        website_config = config[website_name]

        self.url = website_config["url"]
        self.name_selector = website_config["name_selector"]
        self.price_selector = website_config["price_selector"]

        self.driver = None
        self.wait = None

        self.setup_driver()

    
    def setup_driver(self):
        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.wait = WebDriverWait(self.driver, 10)
        except Exception as error:
            print("Error setting up the driver\n", error)
            exit(1)


    @staticmethod
    def extract_website_name(url):
        pattern = r"https?://(?:www\.)?(.*?)\."
        match = re.search(pattern, url)

        if match:
            return match.group(1)
        else:
            return None


    def scrape_data(self):
        try:
            self.driver.get(self.url)
            get_url = self.driver.current_url
            self.wait.until(EC.url_to_be(self.url))

            if get_url == self.url:
                names = self.driver.find_elements(By.CSS_SELECTOR, self.name_selector)
                prices = self.driver.find_elements(By.CSS_SELECTOR, self.price_selector)

            data = []
            for name, price, in zip(names, prices):
                if name.text and price.text:
                    data.append((name.text.replace("Impressora 3D ", "").replace("3D Printer", "").strip(), price.text.replace(",", ".").replace("from $", "").replace("€", "").strip(), self.extract_website_name(self.url).capitalize()))
            return data

        except Exception as error:
            print("Error on scraping data from website\n", error)
            exit(1)

        finally:
            self.driver.quit()
