import requests
from bs4 import BeautifulSoup
import json
import time

# Initialize an empty list to store the links
post_links = []

# Iterate over the range of page numbers
for i in range(1, 61):
    # Construct the URL
    url = f"https://www.livinginsider.com/searchword_en/Condo/Rent/{i}/property-listing-condo-for-rent.html"

    # Make the request and parse the response
    html = requests.get(url)
    s = BeautifulSoup(html.content, 'html.parser')
    results = s.find(class_="panel-body")
    posts = results.find_all('div', class_='item-desc')

    # Extract the links and append them to the list
    for post in posts:
        post_links.append(post.find('div', class_='col-md-12 col-sm-12').find('a')['href'])
    print(str(len(posts)) + " links downloaded.")
    time.sleep(1)
# Load existing links from the file
with open('post_links.json', 'r') as f:
    existing_links = json.load(f)

# Append new links to the existing ones
existing_links.extend(post_links)

# Write the updated list back to the file
with open('post_links.json', 'w') as f:
    json.dump(existing_links, f)

print(str(len(post_links)) + " posts added to post_links.json file.")