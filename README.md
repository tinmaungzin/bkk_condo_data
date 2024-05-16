# Bangkok Condo Rental Prices Data Analysis Project

## Overview:
This project focuses on analyzing rental prices for condos in Bangkok, Thailand. It involves scraping rental listing websites to gather data, downloading the actual rental data, and analyzing it to gain insights into the rental market trends in Bangkok.

## Files Included:

1. **post_link_scrape.py:**
   - This Python script is responsible for scraping rental listing from livinginsider.com to obtain the links to individual condo rental posts.
   - It saves the collected links in a JSON file named `post_links.json`.
   - Usage: Run `python post_link_scrape.py` to execute the script.

2. **post_download.py:**
   - This Python script downloads the actual rental data from the links collected by `post_link_scrape.py`.
   - It fetches details such as rental prices, location, amenities, etc., and saves them in an Excel file named `Condo List.xlsx`.
   - Usage: Run `python post_download.py` to execute the script.

3. **BKK Condo.twb:**
   - This is a Tableau workbook file that contains visualizations and dashboards created from the collected rental data.
   - It provides interactive visualizations for exploring and analyzing the condo rental market trends in Bangkok.

## Usage Instructions:
1. Before running `post_link_scrape.py` and `post_download.py`, ensure that Python and necessary libraries (e.g., BeautifulSoup, requests) are installed.
2. Execute `post_link_scrape.py` to scrape rental listing links and save them to `post_links.json`.
3. Run `post_download.py` to download rental data from the collected links and save it to `Condo List.xlsx`.
4. Open `BKK Condo.twb` using Tableau Desktop to explore the visualizations and dashboards.

## Dependencies:
- Python 3.x
- BeautifulSoup
- Requests
- Tableau Desktop (for viewing Tableau workbook)
