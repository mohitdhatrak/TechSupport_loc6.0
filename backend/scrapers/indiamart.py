import requests
from bs4 import BeautifulSoup
import pprint

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

    price = soup.find('span', class_='bo price-unit').text.strip().split('/')[0]

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
        else:
            print("Table not found within the div tag with class 'dtlsec1'")
    else:
        print("Div tag with class 'dtlsec1' not found")

    img_tag = soup.find('img', class_='img-drift-demo-trigger')
    image_src = img_tag['src']

    result = {
        'source' : 'indiamart',
        'title': title,
        'price': price,
        'description': table_data,
        'image_src': image_src
    }

    return result

url = "https://www.indiamart.com/proddetail/iphone-15-2852413077688.html"
product_data = indiamart_scraper(url)
pprint.pprint(product_data)
