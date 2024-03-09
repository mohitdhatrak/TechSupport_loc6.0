import requests
from bs4 import BeautifulSoup
import json
import re
import pprint
from serpapi import GoogleSearch

# Regular expressions for filtering links
flipkart_pattern = re.compile(r"/p/\w+")
ebay_pattern = re.compile(r"/itm/\d+")
indiamart_pattern = re.compile(r"/proddetail/")

# Main function to extract search results
def extract_search_results(query, platform):
    params = {
        "q": f"Buy {query} at best price {platform}",
        "api_key": " 80f40b48b2e799f40e5bfe9ebbb9f2e0dc267db2da8abb7b2f564fa25148067c"  # Replace this with your actual SerpApi API key
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # Extracting organic search results
    organic_results = results.get("organic_results", [])

    # Filtering and printing titles and URLs of organic search results from the specified platform
    flipkart_links = []
    ebay_links = []
    indiamart_links = []
    for result in organic_results:
        link = result.get("link")
        if link:
            if "/p/" in link or "/buy/" in link or "/proddetail" in link or "/itm" in link:
                if "flipkart" in link:
                    flipkart_links.append(link)
                elif "ebay" in link:
                    ebay_links.append(link)
                elif "indiamart" in link:
                    indiamart_links.append(link)

    return flipkart_links, ebay_links, indiamart_links

# Function to filter links based on platform
def filter_links(links, platform):
    if platform == "flipkart":
        return [link for link in links if flipkart_pattern.search(link)]
    elif platform == "ebay":
        return [link for link in links if ebay_pattern.search(link)]
    elif platform == "indiamart":
        return [link for link in links if indiamart_pattern.search(link)]

# Function to scrape eBay data
def ebay_scraper(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive'
    }

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('h1', class_="x-item-title__mainTitle").text.strip()
    price = soup.find('div', class_="x-price-primary").text.strip()
    info = soup.find('div', class_="ux-layout-section__item").text.strip()

    div_tag = soup.find('div', class_='ux-image-carousel-item')
    image_url = div_tag.find('img')['src'] if div_tag and div_tag.find('img') else ""

    reviews_container = soup.find('div', class_="d-stores-info-categories__details-container__tabbed-list")
    reviews_count = len(reviews_container.find_all(text="Verified purchase")) if reviews_container else 0
    
    description = "lorem ipsum"

    result = {
        'source': 'ebay',
        'title': title,
        'price': price,
        'reviews_count': reviews_count,
        'description': description,
        'image_url': image_url,
    }

    return result

# Function to scrape Flipkart data
def flipkart_scraper(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive'
    }

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    

    title = soup.find('h1', class_="yhB1nd").text.strip()

    img_tag = soup.find('img', class_='_396cs4 _2amPTt _3qGmMb')
    image_src = img_tag['src'] if img_tag else ""

    value = soup.find('span', class_="_2_R_DZ").text.strip()
    split = value.split("&")
    reviews = split[1].split()[0] if len(split) > 1 else "0"

    price = soup.find('div', class_="_30jeq3 _16Jk6d").text.strip()

    highlights_div = soup.find('div', class_='_2cM9lP')
    highlights_list = [li.text.strip() for li in highlights_div.find_all('li')] if highlights_div else []
    
    result = {
        'source': 'Flipkart',
        'title': title,
        'price': price,
        'reviews_count': reviews, 
        'description': highlights_list,
        'image_url': image_src
    }

    return result

# Function to scrape Indiamart data
def indiamart_scraper(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive'
    }

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.find('h1', class_="bo center-heading").text.strip()

    price_element = soup.find('span', class_='bo price-unit')
    price = price_element.text.strip().split('/')[0] if price_element else "Price not available"

    div_tag = soup.find('div', class_='dtlsec1')
    table_data = {}
    if div_tag:
        table = div_tag.find('table')
        if table:
            rows = table.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                if len(cells) == 2:
                    key = cells[0].text.strip()
                    value = cells[1].text.strip()
                    table_data[key] = value

    img_tag = soup.find('img', class_='img-drift-demo-trigger')
    image_src = img_tag['src'] if img_tag else ""
    
    reviews_count = "1851"

    result = {
        'source' : 'indiamart',
        'title': title,
        'price': price,
        'reviews_count': reviews_count,
        'description': table_data,
        'image_url': image_src
    }

    return result

# Main code execution
queries = ["Samsung galaxy s23 ultra"]
platforms = ["flipkart", "ebay", "indiamart"]

# Dictionary to store scraped data for each platform
scraped_data_dict = {"flipkart": [], "ebay": [], "indiamart": []}

for product in queries:
    for platform in platforms:
        flipkart_links, ebay_links, indiamart_links = extract_search_results(product, platform)
        if platform == "flipkart":
            for link in flipkart_links:
                product_data = flipkart_scraper(link)
                scraped_data_dict["flipkart"].append(product_data)
        elif platform == "ebay":
            for link in ebay_links:
                product_data = ebay_scraper(link)
                scraped_data_dict["ebay"].append(product_data)
        elif platform == "indiamart":
            for link in indiamart_links:
                product_data = indiamart_scraper(link)
                scraped_data_dict["indiamart"].append(product_data)

# Convert scraped data dictionary to JSON format
json_data = json.dumps(scraped_data_dict)

# Print the JSON data
print(json_data)
