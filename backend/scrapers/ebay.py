import requests
from bs4 import BeautifulSoup

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
    
    # Scraping product category
    category = soup.find('a', class_="seo-breadcrumb-text")
    product_category = category.text.strip() if category else "Category not found"

    result = {
        'source' : 'ebay',
        'title': title,
        'price': price,
        'image_url': image_url,
        'reviews_count': reviews_count,
        'product_category': product_category
    }

    return result

url = "https://www.ebay.com/itm/196119527515?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D20231107084023%26meid%3Dc68c6a801c474e5381e775c561f5e7d2%26pid%3D101875%26rk%3D1%26rkt%3D4%26sd%3D155780190004%26itm%3D196119527515%26pmt%3D1%26noa%3D1%26pg%3D4429486%26algv%3DSimplAMLv11WebTrimmedV3MskuWithLambda85KnnRecallV1V2V4ItemNrtInQueryAndCassiniVisualRankerAndBertRecallWithVMEV3CPCAutoWithCassiniEmbRecall%26brand%3DApple&_trksid=p4429486.c101875.m1851&itmprp=cksum%3A196119527515c68c6a801c474e5381e775c561f5e7d2%7Cenc%3AAQAIAAABQHD%252FO%252BVoFoPPIoZ2g0kOZxWd85mWuIHekSp3qag7zFfwObZeQoitzE%252FDCfcejfO%252BzOLmzZmy11RrgWpA56KM9DpasK%252BGtGYwCFvgaK6ijP5AqShEUhT8f2oX6hvndJ3G0oWH8DD1DlBWseQltpxcSDW2Uu52NrseaxeINpsrDP6vx7ny%252BkPKauMa3yeSanWiilC5jqhfIQu1hHPSl0Y0TKGCtR3Inlo260BOmOFneCK0cC5eeZFCmJBUEuCKWDGlNgRqXCt6nn7eWKrj1zys87cpHxBRQXwjPR%252B9rBcF3Yy5T8ODcmwWhRexO2AqL6SLiGRxfIcTYPFJu9nFxwTeFhGj1FI3bpdwzcwVv1C8fzXGqGxTE8KOgE7emLQhsT39%252BubDt1jPe7HuBI1nyvsOgNN4nJm5FucAZyZYrPbwn3qj%7Campid%3APLP_CLK%7Cclp%3A4429486&epid=3065007322&itmmeta=01HRH3TJXR2YWH8H4CQNPZXSKP"
product_data = ebay_scraper(url)
print(product_data)
