from datetime import datetime

flipkart_sales = {
    'Big Saving Days': {
        'Expected Date': (datetime(2024, 3, 11), datetime(2024, 3, 15)),
        'Sale Theme': 'Best offers and discounts on mobile, electronics, TVs, appliances, home furnishing, etc.'
    },
    'Appliances Bonanza': {
        'Expected Date': (datetime(2024, 3, 16), datetime(2024, 3, 21)),
        'Sale Theme': 'Offers and discounts on home appliances.'
    },
    'Summer Sale': {
        'Expected Date': (datetime(2024, 3, 22), datetime(2024, 3, 26)),
        'Sale Theme': 'Offers and deals on ACs, coolers, fans and more.'
    },
    'Big Bachat Dhamaal Sale': {
        'Expected Date': (datetime(2024, 4, 1), datetime(2024, 4, 3)),
        'Sale Theme': 'Offers on electronics, discounts on smartphones, TVs, laptops, and more. Deals on fashion, home appliances, home furnishing, home decor and more.'
    },
    'Summer Saver Days': {
        'Expected Date': (datetime(2024, 4, 13), datetime(2024, 4, 17)),
        'Sale Theme': 'Offers and discounts on ACs, coolers, fans and more.'
    },
    'Electronics Sale': {
        'Expected Date': (datetime(2024, 5, 23), datetime(2024, 5, 31)),
        'Sale Theme': 'Best offers on electronics, TVs, laptops, smartphones and more.'
    },
    'End-of-Season Sale': {
        'Expected Date': (datetime(2024, 6, 1), datetime(2024, 6, 6)),
        'Sale Theme': 'Great offers on fashion. 50-80% off on clothing and footwear.'
    },
    'Big Saving Days': {
        'Expected Date': (datetime(2024, 6, 10), datetime(2024, 6, 14)),
        'Sale Theme': 'Best offers and discounts on mobile, electronics, TVs, appliances, home furnishing, home decor, kitchen, fashion, beauty etc.'
    },
    'Grand Home Appliances Sale': {
        'Expected Date': (datetime(2024, 6, 18), datetime(2024, 6, 22)),
        'Sale Theme': 'Good discounts on home appliances such as washing machines, refrigerators, etc.'
    },
    'Big Bachat Dhamaal Sale': {
        'Expected Date': (datetime(2024, 6, 23), datetime(2024, 6, 25)),
        'Sale Theme': 'Offers on electronics, discounts on smartphones, TVs, laptops, fashion, home appliances, home furnishing, home decor, kitchen, beauty, toys and more.'
    },
    'Big Bachat Dhamaal Sale': {
        'Expected Date': (datetime(2024, 7, 1), datetime(2024, 7, 3)),
        'Sale Theme': 'Offers on electronics, discounts on smartphones, TVs, laptops, fashion, home appliances, home furnishing, home decor, kitchen, beauty, toys and more.'
    },
    'Big Saving Days': {
        'Expected Date': (datetime(2024, 7, 15), datetime(2024, 7, 19)),
        'Sale Theme': 'Best offers and discounts on mobile, electronics, TVs, appliances, home furnishing, home decor, kitchen, fashion, beauty, toys, baby care, etc.'
    },
    'Flipkart Big Freedom Sale': {
        'Expected Date': (datetime(2024, 8, 5), datetime(2024, 8, 9)),
        'Sale Theme': 'Discounts and deals on smartphones, TVs, laptops, electronics, home appliances, kitchen, fashion and more.'
    },
    'Independence Day Sale': {
        'Expected Date': (datetime(2024, 8, 12), datetime(2024, 8, 15)),
        'Sale Theme': 'Offers on smartphones, electronics, home appliances, kitchen, fashion, clothing, beauty and more.'
    },
    'Flipkart TV Day Sale': {
        'Expected Date': (datetime(2024, 8, 16), datetime(2024, 8, 18)),
        'Sale Theme': 'Great offers and discounts on TVs and Smart TVs.'
    },
    'Month-End Mobile Fest': {
        'Expected Date': (datetime(2024, 8, 25), datetime(2024, 8, 31)),
        'Sale Theme': 'Offers and deals on best-selling smartphones.'
    },
    'Mega Monsoon Days Sale': {
        'Expected Date': (datetime(2024, 8, 26), datetime(2024, 8, 31)),
        'Sale Theme': 'Best offers on TV, appliances, clothing, groceries and more.'
    },
    'Grand Home Appliances Sale': {
        'Expected Date': (datetime(2024, 9, 7), datetime(2024, 9, 11)),
        'Sale Theme': 'Discounts and deals on home appliances and kitchen appliances.'
    },
    'Budget Dhamaka Sale': {
        'Expected Date': (datetime(2024, 9, 14), datetime(2024, 9, 16)),
        'Sale Theme': 'Offers on TV, appliances, fashion, groceries, kitchen appliances and more.'
    },
    'Flipkart Big Billion Day Sale': {
        'Expected Date': (datetime(2024, 10, 8), datetime(2024, 10, 15)),
        'Sale Theme': 'Biggest deals and discounts on mobiles, electronics, TVs, appliances, home furnishing, home decor, kitchen, fashion, beauty, etc.'
    },
    'Flipkart Big Dussehra Sale': {
        'Expected Date': (datetime(2024, 10, 22), datetime(2024, 10, 29)),
        'Sale Theme': 'Offers on smartphones, TVs, electronics, laptops, tablets, home appliances, kitchen appliances, fashion and more.'
    },
    'Flipkart Big Diwali Sale': {
        'Expected Date': (datetime(2024, 11, 2), datetime(2024, 11, 11)),
        'Sale Theme': 'On the occasion of the Diwali festive season, Flipkart offers big deals and discounts on mobiles, electronics, TVs, appliances, home furnishing, home decor, kitchen, fashion, beauty, etc.'
    },
    'Flipkart Diwali Dhamaka Sale': {
        'Expected Date': (datetime(2024, 11, 12), datetime(2024, 11, 15)),
        'Sale Theme': 'Offers on smartphones, electronics, home appliances, kitchen, fashion, clothing, beauty and more.'
    },
    'Black Friday Sale': {
        'Expected Date': (datetime(2024, 11, 27), datetime(2024, 11, 30)),
        'Sale Theme': 'Sale on multiple categories on the occasion of Black Friday.'
    },
    'Big Bachaat Sale': {
        'Expected Date': (datetime(2024, 12, 1), datetime(2024, 12, 3)),
        'Sale Theme': 'Great discounts and offers on electronics, smartphones, TVs, appliances, fashion and more.'
    },
    'Big Saving Days': {
        'Expected Date': (datetime(2024, 12, 16), datetime(2024, 12, 21)),
        'Sale Theme': 'Best offers and discounts on mobile, electronics, TVs, appliances, home furnishing, etc.'
    },
    'Grand Gadget Days Sale': {
        'Expected Date': (datetime(2024, 12, 29), datetime(2024, 12, 31)),
        'Sale Theme': 'Biggest deals on smartphones, TWS, audio, electronics, TVs, and more.'
    },
    'Flipkart Year-End Sale': {
        'Expected Date': (datetime(2024, 12, 24), datetime(2024, 12, 31)),
        'Sale Theme': 'Best deals on multiple categories such as electronics, smartphones, TVs, tablets, fashion, kitchen, etc.'
    }
}

amazon_sales = {
    'Amazon Great RepublicDay Sale': {
        'Expected Dates': (datetime(2024, 1, 14), datetime(2024, 1, 18)),
        'Product categories': 'Electronic devices, home, kitchen, and appliance',
        'Discounts': '60% off plus 10% on SBI credit card swipes'
    },
    'Grand Gaming Days': {
        'Expected Dates': (datetime(2024, 1, 8), datetime(2024, 1, 30)),
        'Product categories': 'Gaming gadgets',
        'Discounts': '60% off'
    },
    'Valentine’s Day Store': {
        'Expected Dates': (datetime(2024, 2, 2), datetime(2024, 2, 14)),
        'Product categories': 'Tech Products',
        'Discounts': 'Up to 70% off'
    },
    'Amazon Fab Phone Fest': {
        'Expected Dates': (datetime(2024, 2, 22), datetime(2024, 2, 25)),
        'Product categories': 'Various categories',
        'Discounts': '40% off + 10% cash back on big brands'
    },
    'Super Value Days offer': {
        'Expected Dates': (datetime(2024, 3, 1), datetime(2024, 3, 7)),
        'Product categories': 'Everyday supplies and groceries',
        'Discounts': '10% off'
    },
    'Amazon Holi Sale': {
        'Expected Dates': (datetime(2024, 3, 5), datetime(2024, 3, 9)),
        'Product categories': 'Fashion, beauty, appliances, etc.',
        'Discounts': 'Various deals and offers: SBI bank cards offer'
    },
    'Amazon Summer Offer': {
        'Expected Dates': (datetime(2024, 5, 4), datetime(2024, 5, 8)),
        'Product categories': 'Various categories',
        'Discounts': 'Up to 50% off, additional bank offers'
    },
    'Great Indian Summer Sale': {
        'Expected Dates': (datetime(2024, 5, 13), datetime(2024, 5, 17)),
        'Product categories': 'Electronic items',
        'Discounts': 'Up to 70% off'
    },
    'Prime Day Sale': {
        'Expected Dates': (datetime(2024, 7, 26), datetime(2024, 7, 27)),
        'Product categories': 'Several categories',
        'Discounts': 'Various discounts and deals'
    },
    'Great Freedom Fest': {
        'Expected Dates': (datetime(2024, 8, 5), datetime(2024, 8, 9)),
        'Product categories': 'All categories',
        'Discounts': 'Up to 80 % + additional 10% off'
    },
    'Amazon Black Friday Sale': {
        'Expected Dates': (datetime(2024, 11, 22), datetime(2024, 11, 25)),
        'Product categories': 'Fashion, electronics, etc.',
        'Discounts': 'Great discounts'
    },
    'Christmas Offer': {
        'Expected Dates': (datetime(2024, 12, 21), datetime(2024, 12, 25)),
        'Product categories': 'Winter wear',
        'Discounts': 'Discounts and offers'
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

# Print upcoming Flipkart sales
print("Upcoming Flipkart Sales:")
for sale_name, sale_info in upcoming_flipkart_sales.items():
    start_date_text = sale_info['Expected Date'][0].strftime("%dth %B %Y")
    end_date_text = sale_info['Expected Date'][1].strftime("%dth %B %Y")
    print(f"{sale_name}: {start_date_text} - {end_date_text} | {sale_info['Sale Theme']}")

# Print upcoming Amazon sales
print("\nUpcoming Amazon Sales:")
for sale_name, sale_info in upcoming_amazon_sales.items():
    start_date_text = sale_info['Expected Dates'][0].strftime("%dth %B %Y")
    end_date_text = sale_info['Expected Dates'][1].strftime("%dth %B %Y")
    print(f"{sale_name}: {start_date_text} - {end_date_text} | {sale_info['Product categories']}, Discounts: {sale_info['Discounts']}")