import os
import shutil

import bcrypt
import nltk  # Add this import statement
from bson import ObjectId
from config.database import collection_name, user_collection
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from models.todos import Todo
from models.user import UpdateUser, User
from schema.schemas import list_serial
# from transformers import pipeline
import nltk  # Add this import statement
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from schema.schemas import list_serial

nltk.download('vader_lexicon')  # Move this line here
from typing import Dict, List

UPLOAD_DIR = "profile_photos"
import json
import pprint
import random
import re
from datetime import datetime
from typing import Dict

import requests
from bs4 import BeautifulSoup
from serpapi import GoogleSearch

# from ..scrapers.serapi_scraping import ebay_scraper,flipkart_scraper,indiamart_scraper,extract_search_results

generic_reviews = [
    {'name': 'Aarav Kumar', 'stars': 4, 'review': 'Great product, highly recommended! It exceeded my expectations and works flawlessly. The build quality is exceptional, and the features are exactly what I needed. I would definitely buy it again.'},
    {'name': 'Aarya Gupta', 'stars': 5, 'review': 'This product is amazing! I have been using it for a while now, and it has never let me down. The performance is outstanding, and the design is sleek and modern. I would give it 10 stars if I could!'},
    {'name': 'Aarush Singh', 'stars': 3, 'review': 'I purchased this product with high hopes, but it fell a bit short of my expectations. While it gets the job done, it lacks some of the advanced features that similar products offer. Overall, it\'s decent for the price.'},
    {'name': 'Aditi Sharma', 'stars': 4, 'review': 'I am pleasantly surprised by the quality of this product. It is well-built and durable, and it performs admirably. The price is reasonable, and I would definitely recommend it to others.'},
    {'name': 'Aditya Patel', 'stars': 2, 'review': 'Unfortunately, I had a few issues with this product. While it initially worked fine, it started experiencing problems after a few weeks of use. The customer service was helpful, but I expected better reliability from this brand.'},
    {'name': 'Advait Malhotra', 'stars': 5, 'review': 'I absolutely love this product! It has exceeded all my expectations and made my life so much easier. The design is sleek, the performance is top-notch, and the price is unbeatable. I would recommend it to everyone.'},
    {'name': 'Advika Reddy', 'stars': 4, 'review': 'This product is decent for the price, but it has some limitations. It works fine, but it lacks some of the features that similar products offer. Overall, it\'s a good value for the money.'},
    {'name': 'Advik Shah', 'stars': 5, 'review': 'I cannot say enough good things about this product. It is truly outstanding in every way. The performance is exceptional, the design is sleek and modern, and the price is unbeatable. I would recommend it to everyone.'},
    {'name': 'Ahana Nair', 'stars': 4, 'review': 'I am quite happy with this product. It meets all my needs and performs admirably. The price is reasonable, and the build quality is good. Overall, it\'s a solid purchase.'},
    {'name': 'Aiden Choudhury', 'stars': 3, 'review': 'I had high hopes for this product, but it fell short of my expectations. While it works fine, it lacks some of the features that similar products offer. It\'s not bad, but there are better options available.'},
    {'name': 'Aisha Verma', 'stars': 4, 'review': 'I am pleased with this product. It offers good value for the money and performs well. The build quality is decent, and it has all the features I need. Overall, it\'s a solid choice.'},
    {'name': 'Akash Singh', 'stars': 5, 'review': 'I absolutely love this product! It has exceeded all my expectations and made my life so much easier. The performance is outstanding, the design is sleek, and the price is unbeatable. I would recommend it to everyone.'},
    {'name': 'Akhil Patel', 'stars': 4, 'review': 'I am very impressed with this product. It performs admirably and offers good value for the money. The design is sleek, and the build quality is excellent. I would definitely purchase it again.'},
    {'name': 'Akshara Nair', 'stars': 3, 'review': 'This product is decent for the price, but it lacks some of the features that I was hoping for. It gets the job done, but it\'s not exceptional. Overall, it\'s a solid choice if you\'re on a budget.'},
    {'name': 'Akshay Sharma', 'stars': 4, 'review': 'I am satisfied with this product. It performs well and offers good value for the money. The design is sleek, and the build quality is excellent. I would definitely recommend it to others.'}
]


flipkart_sales = {
    'Big Saving Days': {
        'Expected Date': (datetime(2024, 3, 11), datetime(2024, 3, 15)),
        'Sale Theme': ['mobile', 'electronics', 'TVs', 'appliances', 'home furnishing'],
        'percentage_discount': 50
    },
    'Appliances Bonanza': {
        'Expected Date': (datetime(2024, 3, 16), datetime(2024, 3, 21)),
        'Sale Theme': ['home appliances'],
        'percentage_discount': 40
    },
    'Summer Sale': {
        'Expected Date': (datetime(2024, 3, 22), datetime(2024, 3, 26)),
        'Sale Theme': ['ACs', 'coolers', 'fans'],
        'percentage_discount': 30
    },
    'Big Bachat Dhamaal Sale': {
        'Expected Date': (datetime(2024, 4, 1), datetime(2024, 4, 3)),
        'Sale Theme': ['electronics', 'smartphones', 'TVs', 'laptops', 'fashion', 'home appliances', 'home furnishing', 'home decor'],
        'percentage_discount': 45
    },
    'Summer Saver Days': {
        'Expected Date': (datetime(2024, 4, 13), datetime(2024, 4, 17)),
        'Sale Theme': ['ACs', 'coolers', 'fans'],
        'percentage_discount': 35
    },
    'Electronics Sale': {
        'Expected Date': (datetime(2024, 5, 23), datetime(2024, 5, 31)),
        'Sale Theme': ['electronics', 'TVs', 'laptops', 'smartphones'],
        'percentage_discount': 40
    },
    'End-of-Season Sale': {
        'Expected Date': (datetime(2024, 6, 1), datetime(2024, 6, 6)),
        'Sale Theme': ['fashion', 'clothing', 'footwear'],
        'percentage_discount': 60
    },
    'Grand Home Appliances Sale': {
        'Expected Date': (datetime(2024, 6, 18), datetime(2024, 6, 22)),
        'Sale Theme': ['home appliances', 'washing machines', 'refrigerators'],
        'percentage_discount': 50
    },
    'Flipkart Big Freedom Sale': {
        'Expected Date': (datetime(2024, 8, 5), datetime(2024, 8, 9)),
        'Sale Theme': ['smartphones', 'TVs', 'laptops', 'electronics', 'home appliances', 'kitchen', 'fashion'],
        'percentage_discount': 50
    },
    'Flipkart Big Billion Day Sale': {
        'Expected Date': (datetime(2024, 10, 8), datetime(2024, 10, 15)),
        'Sale Theme': ['mobiles', 'electronics', 'TVs', 'appliances', 'home furnishing', 'home decor', 'kitchen', 'fashion'],
        'percentage_discount': 70
    },
    'Flipkart Big Dussehra Sale': {
        'Expected Date': (datetime(2024, 10, 22), datetime(2024, 10, 29)),
        'Sale Theme': ['smartphones', 'TVs', 'electronics', 'laptops', 'tablets', 'home appliances', 'kitchen appliances', 'fashion'],
        'percentage_discount': 60
    },
    'Flipkart Big Diwali Sale': {
        'Expected Date': (datetime(2024, 11, 2), datetime(2024, 11, 11)),
        'Sale Theme': ['mobiles', 'electronics', 'TVs', 'appliances', 'home furnishing', 'home decor', 'kitchen', 'fashion'],
        'percentage_discount': 70
    },
    'Flipkart Diwali Dhamaka Sale': {
        'Expected Date': (datetime(2024, 11, 12), datetime(2024, 11, 15)),
        'Sale Theme': ['smartphones', 'electronics', 'home appliances', 'kitchen', 'fashion', 'clothing', 'beauty'],
        'percentage_discount': 50
    },
    'Big Saving Days': {
        'Expected Date': (datetime(2024, 12, 16), datetime(2024, 12, 21)),
        'Sale Theme': ['mobile', 'electronics', 'TVs', 'appliances', 'home furnishing'],
        'percentage_discount': 50
    },
    'Grand Gadget Days Sale': {
        'Expected Date': (datetime(2024, 12, 29), datetime(2024, 12, 31)),
        'Sale Theme': ['smartphones', 'TWS', 'audio', 'electronics', 'TVs'],
        'percentage_discount': 40
    },
    'Flipkart Year-End Sale': {
        'Expected Date': (datetime(2024, 12, 24), datetime(2024, 12, 31)),
        'Sale Theme': ['electronics', 'smartphones', 'TVs', 'tablets', 'fashion', 'kitchen'],
        'percentage_discount': 60
    }
}

amazon_sales = {
    'Amazon Great RepublicDay Sale': {
        'Expected Dates': (datetime(2024, 1, 14), datetime(2024, 1, 18)),
        'Product categories': ['Electronic devices', 'home', 'kitchen', 'appliance'],
        'percentage_discount': 60
    },
    'Grand Gaming Days': {
        'Expected Dates': (datetime(2024, 1, 8), datetime(2024, 1, 30)),
        'Product categories': ['Gaming gadgets'],
        'percentage_discount': 60
    },
    'Valentine’s Day Store': {
        'Expected Dates': (datetime(2024, 2, 2), datetime(2024, 2, 14)),
        'Product categories': ['Tech Products'],
        'percentage_discount': 70
    },
    'Amazon Fab Phone Fest': {
        'Expected Dates': (datetime(2024, 2, 22), datetime(2024, 2, 25)),
        'Product categories': ['Various categories'],
        'percentage_discount': 40
    },
    'Super Value Days offer': {
        'Expected Dates': (datetime(2024, 3, 1), datetime(2024, 3, 7)),
        'Product categories': ['Everyday supplies and groceries'],
        'percentage_discount': 10
    },
    'Amazon Holi Sale': {
        'Expected Dates': (datetime(2024, 3, 5), datetime(2024, 3, 9)),
        'Product categories': ['Fashion', 'beauty', 'appliances'],
        'percentage_discount': 50
    },
    'Amazon Summer Offer': {
        'Expected Dates': (datetime(2024, 5, 4), datetime(2024, 5, 8)),
        'Product categories': ['Various categories'],
        'percentage_discount': 50
    },
    'Great Indian Summer Sale': {
        'Expected Dates': (datetime(2024, 5, 13), datetime(2024, 5, 17)),
        'Product categories': ['Electronic items'],
        'percentage_discount': 70
    },
    'Prime Day Sale': {
        'Expected Dates': (datetime(2024, 7, 26), datetime(2024, 7, 27)),
        'Product categories': ['Several categories'],
        'percentage_discount': 40
    },
    'Great Freedom Fest': {
        'Expected Dates': (datetime(2024, 8, 5), datetime(2024, 8, 9)),
        'Product categories': ['All categories'],
        'percentage_discount': 80
    },
    'Amazon Black Friday Sale': {
        'Expected Dates': (datetime(2024, 11, 22), datetime(2024, 11, 25)),
        'Product categories': ['Fashion', 'electronics'],
        'percentage_discount': 60
    },
    'Christmas Offer': {
        'Expected Dates': (datetime(2024, 12, 21), datetime(2024, 12, 25)),
        'Product categories': ['Winter wear'],
        'percentage_discount': 40
    }
}

# Regular expressions for filtering links
flipkart_pattern = re.compile(r"/p/\w+")
ebay_pattern = re.compile(r"/itm/\d+")
indiamart_pattern = re.compile(r"/proddetail/")

# Main function to extract search results
def extract_search_results(query, platform):
    params = {
        "q": f"Buy {query} at best price {platform}",
        "api_key": "86016d52aec6be86cc6151eed46d5fe704cb3aafc83cbd0a18d8e3538c8192eb"  # Replace this with your actual SerpApi API key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    # print(params)
    # print(results)
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

def calculate_average_sentiment(products: List[Dict]):
    total_reviews = 0
    total_sentiment = 0

    for product in products:
        for review in product['user_reviews']:
            total_reviews += 1
            total_sentiment += review['stars']
    
    if total_reviews == 0:
        return 0  # Avoid division by zero
    else:
        return round(total_sentiment / total_reviews, 2)

def analyze_user_reviews(products: List[Dict]):
    reviews_analysis = []

    for product in products:
        product_analysis = {
            "title": product["title"],
            "average_sentiment": calculate_average_sentiment([product]),
            "positive_reviews": [],
            "negative_reviews": []
        }

        for review in product['user_reviews']:
            if review['stars'] >= 4:
                product_analysis['positive_reviews'].append(review)
            else:
                product_analysis['negative_reviews'].append(review)
        
        reviews_analysis.append(product_analysis)
    
    return reviews_analysis
# Function to scrape eBay data
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

    title_element = soup.find('h1', class_="x-item-title__mainTitle")
    title = title_element.text.strip() if title_element else "Title not found"

    price_element = soup.find('div', class_="x-price-primary")
    price = price_element.text.strip() if price_element else "Price not found"

    info_element = soup.find('div', class_="ux-layout-section__item")
    info = info_element.text.strip() if info_element else "Info not found"

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
    reviews_count = len(reviews_container.find_all(text="Verified purchase")) if reviews_container else 0
    
    description = "lorem ipsum"
    
    user_reviews = random.sample(generic_reviews, 4) 
    
    # Scraping product category
    category = soup.find('a', class_="seo-breadcrumb-text")
    product_category = category.text.strip() if category else "Category not found"

    result = {
        'source': 'ebay',
        'title': title,
        'price': price,
        'reviews_count': reviews_count,
        'description': description,
        'image_url': image_url,
        'user_reviews': user_reviews,
        'product_category': product_category,
        'url': url  # Include the URL
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
    
    title = soup.find('h1', class_="yhB1nd").text.strip()

    img_tag = soup.find('img', class_='_396cs4 _2amPTt _3qGmMb')
    image_src = img_tag['src'] if img_tag else ""

    value = soup.find('span', class_="_2_R_DZ").text.strip()
    split = value.split("&")
    reviews = split[1].split()[0] if len(split) > 1 else "0"

    price = soup.find('div', class_="_30jeq3 _16Jk6d").text.strip()

    highlights_div = soup.find('div', class_='_2cM9lP')
    highlights_list = [li.text.strip() for li in highlights_div.find_all('li')] if highlights_div else []
    
    user_reviews = random.sample(generic_reviews, 4)
    
    category_div = soup.find_all('a', class_="_2whKao")
    j = []
    for i in category_div:
        j.append(i.text)
        
    category = j[1]
    
    result = {
        'source': 'Flipkart',
        'title': title,
        'price': price,
        'reviews_count': reviews, 
        'description': highlights_list,
        'image_url': image_src,
        'user_reviews': user_reviews,
        'product_category': category,
        'url': url  # Include the URL
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
    
    title_tag = soup.find('h1', class_="bo center-heading")
    title = title_tag.text.strip() if title_tag else ""

    # Get price
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
    
    user_reviews = random.sample(generic_reviews, 4)
    
    category_element = soup.find('div', class_="fs12 pb10 mt10 vcrmb")

    # Check if category_element is not None
    if category_element:
        category = category_element.text
    else:
        category = ''

    # Initialize desired_content with an empty string
    desired_content = ""

    # If category is not an empty string, proceed with extracting the desired content
    if category:
        first_index = category.find('>')
        
        # Find the index of the next '>' character after the first one
        second_index = category.find('>', first_index + 1)
        
        # Extract the desired content if the indices are valid
        if first_index != -1 and second_index != -1:
            desired_content = category[first_index + 2:second_index].strip()
        else:
            print("Desired content cannot be extracted due to invalid indices.")
    else:
        print("Category is empty.")

    result = {
        'source' : 'indiamart',
        'title': title,
        'price': price,
        'reviews_count': reviews_count,
        'description': table_data,
        'image_src': image_src,
        'user_reviews': user_reviews,
        'product_category': desired_content,
        'url': url  # Include the URL
    }

    return result
    

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)
router = APIRouter()
# model = pipeline("sentiment-analysis")

# Authentication function
async def authenticate_user(username: str, password: str):
    user_data = user_collection.find_one({"username": username})
    if user_data:
        hashed_password = user_data.get("password", "")
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            return True
    return False

# Error handling
def get_current_user(user: User = Depends(authenticate_user)):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    return user

@router.post("/average_sentiment")
async def average_sentiment(product_data: Dict):
    sentiment_scores = {}

    if product_data.get('flipkart'):
        sentiment_scores['flipkart'] = calculate_average_sentiment(product_data['flipkart'])
    
    if product_data.get('ebay'):
        sentiment_scores['ebay'] = calculate_average_sentiment(product_data['ebay'])
    
    if product_data.get('indiamart'):
        sentiment_scores['indiamart'] = calculate_average_sentiment(product_data['indiamart'])
    
    return sentiment_scores
# Signup route
@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: User):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    user_data = user.dict()
    user_data['password'] = hashed_password
    user_collection.insert_one(user_data)
    return {"message": "User created successfully"}

# Login route
@router.post("/login")
async def login(user: User):
    if await authenticate_user(user.username, user.password):
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

# Update user endpoint
@router.put("/user/{user_id}")
async def update_user(user_id: str, updated_user: UpdateUser, current_user: User = Depends(get_current_user)):
    result = user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": updated_user.dict()})
    if result.modified_count == 1:
        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

# Delete user endpoint
@router.delete("/user/{user_id}")
async def delete_user(user_id: str, current_user: User = Depends(get_current_user)):
    result = user_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 1:
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@router.get("/search_users/{username}")
async def search_users(username: str):
    users = user_collection.find({"username": {"$regex": username, "$options": "i"}})
    if users:
        # Convert ObjectId to string for serialization
        users = [user | {"_id": str(user["_id"])} for user in users]
        return users
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found with the provided username")
    

@router.post("/upload_profile_photo/{user_id}")
async def upload_profile_photo(user_id: str, file: UploadFile = File(...)):
    # Generate a unique filename for the uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    # Save the uploaded file to disk
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Update the user record in the database with the file path of the uploaded photo
    result = user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": {"profile_photo": file_path}})
    
    # Check if the user record was updated successfully
    if result.modified_count == 1:
        return {"message": "Profile photo uploaded successfully"}
    else:
        # If the user record was not updated, delete the uploaded file
        os.remove(file_path)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
# Todo endpoints
@router.get("/")
async def greeting():
   return {'message':'hello world'}

@router.post("/")
async def post_todo(todo:Todo):
    collection_name.insert_one(dict(todo))
    
@router.put("/{id}")
async def put_todo(id:str,todo:Todo):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(todo)})
    
@router.delete("/{id}")
async def delete_todo(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})

@router.post("/get_sales/")
async def get_sales(product_object: dict):
    matching_sales = []
    
    # Extract product category
    product_category = product_object.get('flipkart')[0]['product_category']

    # Check for matching sales in Flipkart using regex
    for sale_name, sale_info in flipkart_sales.items():
        for theme in sale_info['Sale Theme']:
            if any(re.search(re.escape(category), theme, re.IGNORECASE) for category in product_category.split(' & ')):
                matching_sales.append({
                    "platform": "Flipkart",
                    "sale_name": sale_name,
                    "expected_dates": [sale_info['Expected Date'][0].strftime("%dth %B %Y"), sale_info['Expected Date'][1].strftime("%dth %B %Y")],
                    "percentage_discount": sale_info['percentage_discount']
                })

    # Check for matching sales in Amazon using regex
    for sale_name, sale_info in amazon_sales.items():
        for category in sale_info['Product categories']:
            if any(re.search(re.escape(category), product_category, re.IGNORECASE) for category in product_category.split(' & ')):
                matching_sales.append({
                    "platform": "Amazon",
                    "sale_name": sale_name,
                    "expected_dates": [sale_info['Expected Dates'][0].strftime("%dth %B %Y"), sale_info['Expected Dates'][1].strftime("%dth %B %Y")],
                    "percentage_discount": sale_info['percentage_discount']
                })

    return matching_sales
@router.get("/product/")
async def get_product_data(title: str):
    # Perform search and scrape data for the given title
    scraped_data_dict = {"flipkart": [], "ebay": [], "indiamart": []}
    platforms = ["flipkart", "ebay", "indiamart"]
    for platform in platforms:
        flipkart_links, ebay_links, indiamart_links = extract_search_results(title, platform)
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
    
    # Check if any data has been scraped
    if not any(scraped_data_dict.values()):
        raise HTTPException(status_code=404, detail="No products found")

    return scraped_data_dict

    