import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://goldpricez.com/in/gram"  # Replace with a valid gold price website

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the element containing the gold price (update the selector based on the website's structure)
    gold_price = soup.find('span', class_='display_rates_bid')  # Replace with the actual tag and class
    
    if gold_price:
        print(f"Current Gold Price in India: {gold_price.text.strip()}")
    else:
        print("Could not find the gold price on the page.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")