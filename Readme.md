# Web Scraper for Midwifery Today Conferences

This project contains a Python-based web scraper that extracts data about past conferences from [Midwifery Today](https://www.midwiferytoday.com/). The extracted data includes the place, title, and time of each conference, which is then saved to a CSV file.

## Features

- Uses Selenium to navigate to the "Past Conferences" page.
- Extracts conference data using BeautifulSoup.
- Filters out irrelevant data and entries.
- Saves the extracted data to a CSV file.

## Requirements

- Python 3
- Selenium
- BeautifulSoup
- Requests

You can install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```
After execution, the extracted data will be saved as conferences.csv in the data directory.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
