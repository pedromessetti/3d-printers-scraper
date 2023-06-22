from scraper import Scraper
from database import create_table, save_data
from datetime import datetime

# Create the table if it doesn't exist
create_table()

scraper = Scraper('https://www.worten.pt/informatica-e-acessorios/impressao/impressoras-3d-e-consumiveis/impressoras-3d')

# Scrape data
data = scraper.scrape_data()

# Get the current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Add timestamp to each data entry
data_with_timestamp = [(name, price, timestamp, website) for name, price, website in data]

# Save data to the database
save_data(data_with_timestamp)
