import pprint
import requests
from bs4 import BeautifulSoup

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

    # Find all img tags and filter based on src attribute starting with "https"
    img_tags = soup.find_all('img', src=lambda src: src and src.startswith('https'))
    if img_tags:
        image_src = img_tags[0].get('src') # Get the src attribute of the first img tag
        data['image'] = image_src

    value = soup.find('span', class_="_2_R_DZ").text.strip()
    split = value.split("&")
    ratings = split[0].split()[0]
    reviews = split[1].split()[0]
    data['reviews'] = reviews

    stars = soup.find('div', class_="_3LWZlK").text
    data['stars'] = stars

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

url = "https://www.flipkart.com/nike-air-max-command-men-s-shoes-running-men/p/itm43805916166ed?pid=SHOGRSTUCNHDZHGZ&lid=LSTSHOGRSTUCNHDZHGZ8ZNQDT&marketplace=FLIPKART&store=osp%2Fcil"
product_data = flipkart_scraper(url)
pprint.pprint(product_data)
