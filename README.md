<h1 align="center">
3D PRINTERS SCRAPER
</h1>

## Index
- [Index](#index)
- [Description :clipboard:](#description-clipboard)
- [Installation :package:](#installation-package)
- [Configuration :wrench:](#configuration-wrench)
- [Usage :computer:](#usage-computer)
- [Contributing](#contributing)
- [Author](#author)

## Description :clipboard:
<p>

This is a Python script that scrapes data from multiple websites and saves it to a database. The script is designed to run periodically to keep the database up-to-date with the latest printer prices.

</p>

## Installation :package:

<p>

To use the script, you need to have Python3 installed on your system. And the the following modules:
- configparser
- datetime
- sqlite3
- selenium

        pip install configparser datetime sqlite3 selenium

</p>


## Configuration :wrench:

<p>

The script reads the website names from a configuration file called config.ini. You can add or remove websites from this file as needed. Each website should have its own section in the file, with the following keys:

- `url`: The URL of the website that you want to scrape
- `name_selector`: The CSS Selector for the printers name
- `price_selector`: The CSS Selector for the printers prices

Example of `config.ini`:
        
        [website1]
        url = https://www.website1.com/printers
        name_selector = h2.printer-name
        price_selector = span.price
        
        [website2]
        url = https://www.website2.com/printers
        name_selector = h3.printer-name
        price_selector = div.price

</p>

## Usage :computer:

<p>

To run the script, simply execute the `main.py` file:

    python main.py

The script will scrape data from each website listed in the `config.ini` file and save it to a SQLite database called `printers.db`. If the `printers` table does not exists in the database, the script will create automatically.

</p>

## Contributing

If you find a bug or have a suggestion for how to improve this script, please open an issue or submit a pull request on GitHub.

## Author

| [<img src="https://avatars.githubusercontent.com/u/105685220?v=4" width=115><br><sub>Pedro Vinicius Messetti</sub>](https://github.com/pedromessetti) |
| :---------------------------------------------------------------------------------------------------------------------------------------------------: |