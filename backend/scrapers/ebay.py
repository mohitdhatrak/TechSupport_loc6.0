import requests
from bs4 import BeautifulSoup
import pprint

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
    image_url = ""
    if div_tag:
        img_tag = div_tag.find('img')
        if img_tag:
            image_url = img_tag['src']
        else:
            print("No image found within the specified div tag")
    else:
        print("No div tag found with the specified class")

    reviews_container = soup.find('div', class_="d-stores-info-categories__details-container__tabbed-list")

    reviews_count = 0
    if reviews_container:
        raw_reviews = reviews_container.text.strip()
        reviews = raw_reviews.split("Verified purchase")[1:]
        reviews_count = len(reviews)

    result = {
        'source' : 'ebay',
        'title': title,
        'price': price,
        'image_url': image_url,
        'reviews_count': reviews_count
    }

    return result

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
    
    data = {'source': 'Flipkart'}

    title = soup.find('h1', class_="yhB1nd").text
    data['title'] = title

    img_tag = soup.find('img', class_='_396cs4 _2amPTt _3qGmMb')
    image_src = img_tag['src']
    data['image'] = image_src

    value = soup.find('span', class_="_2_R_DZ").text.strip()
    split = value.split("&")
    ratings = split[0].split()[0]
    reviews = split[1].split()[0]
    # data['ratings'] = ratings
    data['reviews'] = reviews

    stars = soup.find('div', class_="_3LWZlK").text
    # data['stars'] = stars

    price = soup.find('div', class_="_30jeq3 _16Jk6d").text
    data['price'] = price

    highlights_div = soup.find('div', class_='_2cM9lP')
    if highlights_div:
        highlights_title_div = highlights_div.find('div', class_='_3a9CI2')
        highlights_ul = highlights_div.find('ul')
        highlights_title = highlights_title_div.text.strip() if highlights_title_div else None
        highlights_list = [li.text.strip() for li in highlights_ul.find_all('li')] if highlights_ul else []
        data['description'] = highlights_list

    return data

def extract_search_results(query, platform):
    params = {
        "q": f"Buy {query} at best price {platform}",
        "api_key": "2145d6d7b13649473c8fc27db3144a1fcd104d599cb85342faefc7e612e243ca"  # Replace this with your actual SerpApi API key
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

queries = ["Iphone 15"]
platforms = ["flipkart", "ebay", "indiamart"]

for product in queries:
    for platform in platforms:
        print(f"Results for: {platform} {product}")
        flipkart_links, ebay_links, indiamart_links = extract_search_results(product, platform)
        if platform == "flipkart":
            for link in flipkart_links:
                product_data = flipkart_scraper(link)
                pprint.pprint(product_data)
        elif platform == "ebay":
            for link in ebay_links:
                product_data = ebay_scraper(link)
                pprint.pprint(product_data)
        print("\n")
