import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def extract_website_name(url):
    pattern = r"https?://(?:www\.)?(.*?)\."
    match = re.search(pattern, url)
    
    if match:
        return match.group(1)
    else:
        return None

class Scraper:
    def __init__(self, url):
        self.url = url

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
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

            wait = WebDriverWait(driver, 10)
            driver.get(self.url)
            get_url = driver.current_url
            wait.until(EC.url_to_be(self.url))

            if get_url == self.url:
                names = driver.find_elements(By.CSS_SELECTOR, "span.produc-card__name__link")
                prices = driver.find_elements(By.CSS_SELECTOR, "span.value")

            data = []
            for name, price, in zip(names, prices):
                data.append((name.text, price.text, self.extract_website_name(self.url)))

            driver.quit()

            return data
        except Exception as error:
            print("Error on scraping data from website\n", error)
            exit(1)
