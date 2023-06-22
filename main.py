from scraper import Scraper
from database import create_table, save_data, table_exists
from datetime import datetime

# Create the table if it doesn't exist
if (not table_exists("printers")):
    create_table()

scraper_worten = Scraper('https://www.worten.pt/informatica-e-acessorios/impressao/impressoras-3d-e-consumiveis/impressoras-3d',  '.produc-card__name__link','.value')
scraper_fnac = Scraper('https://www.fnac.pt/SearchResult/ResultList.aspx?Search=impressoras+3d&sft=1&sa=0', '.Article-title', '.userPrice')
scraper_creality = Scraper('https://store.creality.com/eu/collections/3d-printers?spm=..index.header_1.1', '.album-product-surplus-title', '.product-price')

# Scrape data
data = scraper_worten.scrape_data()

# Get the current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Add timestamp to each data entry
data_with_timestamp = [(name, price, timestamp, website) for name, price, website in data]

# Save data to the database
save_data(data_with_timestamp)
