import requests
from bs4 import BeautifulSoup
import csv
import json

def scrape_website():
    url = input("Enter the website URL to scrape: ").strip()
    tag = input("Enter the HTML tag to extract (e.g., h1, h2, p, a): ").strip()
    class_name = input("Enter the class name (optional, press Enter to skip): ").strip()

    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    if class_name:
        elements = soup.find_all(tag, class_=class_name)
    else:
        elements = soup.find_all(tag)

    if not elements:
        print(f"No elements found for <{tag}> with class '{class_name}'")
        return

    data = []
    for el in elements:
        text = el.get_text(strip=True)
        if text:
            data.append({'tag': tag, 'text': text})

    # Export to CSV
    csv_file = 'scraped_data.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['tag', 'text'])
        writer.writeheader()
        writer.writerows(data)

    # Export to JSON
    json_file = 'scraped_data.json'
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print(f"\n✅ Successfully scraped {len(data)} elements.")
    print(f"📄 Data saved to {csv_file} and {json_file}.")

# Run the scraper
scrape_website()
import requests
from bs4 import BeautifulSoup
import csv
import json

def scrape_website():
    url = input("Enter the website URL to scrape: ").strip()
    tag = input("Enter the HTML tag to extract (e.g., h1, h2, p, a): ").strip()
    class_name = input("Enter the class name (optional, press Enter to skip): ").strip()

    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    if class_name:
        elements = soup.find_all(tag, class_=class_name)
    else:
        elements = soup.find_all(tag)

    if not elements:
        print(f"No elements found for <{tag}> with class '{class_name}'")
        return

    data = []
    for el in elements:
        text = el.get_text(strip=True)
        if text:
            data.append({'tag': tag, 'text': text})

    # Export to CSV
    csv_file = 'scraped_data.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['tag', 'text'])
        writer.writeheader()
        writer.writerows(data)

    # Export to JSON
    json_file = 'scraped_data.json'
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print(f"\n✅ Successfully scraped {len(data)} elements.")
    print(f"📄 Data saved to {csv_file} and {json_file}.")

# Run the scraper
scrape_website()
