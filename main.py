import configparser
from scraper import Scraper
from database import create_table, save_data, table_exists
from datetime import datetime


# Read the websites names from the config file
config = configparser.ConfigParser()
config.read("config.ini")
website_names = config.sections()

# Create the table if it doesn't exist
if (not table_exists("printers")):
    create_table()

# Scrape data
data = []
for website_name in website_names:
    scraper = Scraper(website_name)
    data += scraper.scrape_data()

# Get the current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Add timestamp to each data entry
data_with_timestamp = [(name, price, timestamp, website) for name, price, website in data]

# Save data to the database
save_data(data_with_timestamp)
