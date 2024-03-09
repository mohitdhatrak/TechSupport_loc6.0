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
    
    # Extracting product category
    category_div = soup.find_all('a', class_="_2whKao")
    j = []
    for i in category_div:
        j.append(i.text)
        
    category = j[1]
    
    data['product_category'] = category

    return data

url = "https://www.flipkart.com/samsung-galaxy-f15-5g-groovy-violet-128-gb/p/itm3e7d6c7112d45?pid=MOBGYBAVW8HTJH4X&lid=LSTMOBGYBAVW8HTJH4X9VTKYN&marketplace=FLIPKART&q=samsung+galazy&store=search.flipkart.com&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=7f49d0fb-cd4b-4d9f-890c-842a4fb14fb9.MOBGYBAVW8HTJH4X.SEARCH&ppt=sp&ppn=sp&ssid=4v476gzp6o0000001709913269065&qH=5068949f63f423e0"
product_data = flipkart_scraper(url)
pprint.pprint(product_data)
