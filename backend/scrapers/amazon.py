from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint

def returnAmazon():
    # Set up the Chrome driver
    driver = webdriver.Chrome()
    
    # Navigate to the Amazon product page
    driver.get("https://www.amazon.in/OnePlus-Nord-Chromatic-128GB-Storage/dp/B0BY8MCQ9S")
    
    # Wait for the product title to be visible
    wait = WebDriverWait(driver, 10)  # Increased timeout duration to 10 seconds
    product_title_element = wait.until(EC.visibility_of_element_located((By.ID, "productTitle")))
    
    # Extract the product title
    product_title = product_title_element.text.strip()
    
    # Find the price element
    price_element = driver.find_element(By.XPATH, '//span[@class="a-offscreen"]')
    price_text = price_element.text.strip()
    
    # Find the highlights element
    highlights_element = driver.find_element(By.XPATH, '//ul[@class="a-unordered-list a-vertical a-spacing-mini"]')
    
    # Find all <li> elements within the highlights element
    highlights_li = highlights_element.find_elements(By.TAG_NAME, 'li')
    
    # Extract text from each <li> element
    highlights = [li.text.strip() for li in highlights_li]
    
    # Find the rating element
    rating_element = driver.find_element(By.XPATH, '//span[@data-hook="rating-out-of-text"]')
    
    # Get the text content of the rating element
    rating_text = rating_element.text.strip()
    
    # Extract the numeric rating value
    rating = float(rating_text.split()[0])
    
    # Create a dictionary to store the data
    data = {
        "source" : 'amazon',
        "title": product_title,
        "price": price_text,
        "description": highlights,
        "rating": rating
    }
    
    # Close the driver
    driver.quit()
    
    return data

# Call the function to scrape Amazon data
amazon_data = returnAmazon()
pprint.pprint(amazon_data)
