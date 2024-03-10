from datetime import datetime

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

current_date_time = datetime.now()

upcoming_flipkart_sales = {}
upcoming_amazon_sales = {}

# Flipkart sales
for sale_name, sale_info in flipkart_sales.items():
    start_date, end_date = sale_info['Expected Date']
    if current_date_time < start_date:
        upcoming_flipkart_sales[sale_name] = sale_info

# Amazon sales
for sale_name, sale_info in amazon_sales.items():
    start_date, end_date = sale_info['Expected Dates']
    if current_date_time < start_date:
        upcoming_amazon_sales[sale_name] = sale_info

# Print all Flipkart sales
print("Upcoming Flipkart Sales:")
for sale_name, sale_info in upcoming_flipkart_sales.items():
    start_date_text = sale_info['Expected Date'][0].strftime("%dth %B %Y")
    end_date_text = sale_info['Expected Date'][1].strftime("%dth %B %Y")
    print(f"Sale Name: {sale_name}")
    print(f"Expected Dates: {start_date_text} - {end_date_text}")
    print(f"Sale Theme: {', '.join(sale_info['Sale Theme'])}")
    print(f"Percentage Discount: {sale_info['percentage_discount']}%\n")

# Print all Amazon sales
print("Upcoming Amazon Sales:")
for sale_name, sale_info in upcoming_amazon_sales.items():
    start_date_text = sale_info['Expected Dates'][0].strftime("%dth %B %Y")
    end_date_text = sale_info['Expected Dates'][1].strftime("%dth %B %Y")
    print(f"Sale Name: {sale_name}")
    print(f"Expected Dates: {start_date_text} - {end_date_text}")
    print(f"Product Categories: {', '.join(sale_info['Product categories'])}")
    print(f"Percentage Discount: {sale_info['percentage_discount']}%\n")



