import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = 'https://www.worten.pt/informatica-e-acessorios/impressao/impressoras-3d-e-consumiveis/impressoras-3d'
wait = WebDriverWait(driver, 10)
driver.get(url)
get_url = driver.current_url
wait.until(EC.url_to_be(url))

if get_url == url:
    names = driver.find_elements(By.CSS_SELECTOR, "span.produc-card__name__link")
    prices = driver.find_elements(By.CSS_SELECTOR, "span.value")

data = []
for name, price in zip(names, prices):
    data.append([name.text, price.text])

driver.quit()

# Write data to a CSV file
csv_file = "3d_printer_info.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price"])
    writer.writerows(data)

print(f"Data saved to {csv_file}")
