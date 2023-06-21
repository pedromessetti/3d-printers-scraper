import sqlite3
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

# fazer campo de status para manter o track das impressoras availables
# add id nos data

data = []
for name, price in zip(names, prices):
    data.append((name.text, price.text))

driver.quit()

# Create a SQLite database connection
conn = sqlite3.connect("printers.db")

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table to store the data
cursor.execute("CREATE TABLE IF NOT EXISTS printers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price TEXT, status TEXT)")


# Insert data into the table
cursor.executemany("INSERT INTO printers VALUES (?, ?)", data)

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()

print("Data saved to SQLite database.")
