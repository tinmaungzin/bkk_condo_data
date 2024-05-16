import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd
import json
import time
import datetime

pp = pprint.PrettyPrinter(indent=4)
counter = 1

# Load the links from the JSON file
with open('post_links.json', 'r') as f:
    post_links = json.load(f)

# Loop through the links
for j, url in enumerate(post_links):
    html = requests.get(url)
    s= BeautifulSoup(html.content, 'html.parser')
    results = s.find(class_="main-detail-content")
    if results is None:
        print(f"No main detail content found for URL: {url}")
        continue
    name = results.find('span', class_='text_project_detail_green')
    building_type = results.find('div', class_='box-tag-detail')
    post_type = results.find('span', class_='box-tag-detail')
    original_price = results.find('span', class_='txt-before-disc')
    final_price = results.find('span', class_='price-detail')
    price_per_unit = results.find('span', class_='mint-green')
    stats = results.find_all('span', class_='detail-property-list-text')
    description = results.find('p', class_='wordwrap')
    project_detail = results.find('div', class_='detail-text-project')
    location_detail = results.find('div', class_='detail-text-zone')
    map_link = results.find('a', class_='detail-view-map')
    transits = results.find_all('li', attrs={'data-map': 'living_transit'})
    
    # print(transits)
    id = f"{counter}_{datetime.datetime.now().strftime('%Y%m%d')}"

    post_data ={
        'ID': id,
        'Post Title': name.text.strip(),
        'Building Type': building_type.text.strip(),
        'Post Type': post_type.text.strip(),
        'Related posts in this project': project_detail.find('a')['href'],
        'Project Name': project_detail.find('a').text.strip(),
        'Related posts in this location': location_detail.find('a')['href'],
        'Location Name': location_detail.find('a').text.strip(),
        'Map Link': map_link['href'],
        'Original Price': original_price.text.strip().replace('฿', '').replace(',', '').replace('/mo', '').strip(),
        'Final Price': final_price.text.strip().replace('฿', '').replace(',', '').replace('/mo', '').strip(),
        'Price Per Unit': price_per_unit.text.strip().replace('(', '').replace('B./Sq.m.)', '').strip(),
        'Area': ' '.join(stats[0].text.split()).replace('Sq.m.', '').strip(),
        'Level': stats[1].text.strip(),
        'Bedroom': stats[2].text.strip(),
        'Bathroom': stats[3].text.strip(),
        'Description': description.text.strip()
    }
    for i, transit in enumerate(transits, start=1):
        transit_info = {
            'title': transit['title'],
            'latitude': transit['data-lat'],
            'longitude': transit['data-lng'],
            'distance': transit.find('p').text.strip().replace('Km.', '').strip(),
            'mode': transit['data-mode']
        }
        # Add transit details to post_data
        post_data[f'Transit {i}'] = transit_info['title']
        post_data[f'Transit {i} Distance'] = transit_info['distance']
        if(i == 1):
            post_data['Transit 1 Lat'] = transit_info['latitude']
            post_data['Transit 1 Long'] = transit_info['longitude']
    df = pd.DataFrame([post_data])
    existing_data = pd.read_excel('Condo List.xlsx')
    updated_data = existing_data._append(df, ignore_index=True)
    updated_data.to_excel('Condo List.xlsx', index=False)
    print(f'Data added to Condo List.xlsx file. {j+1}')
    time.sleep(1)

