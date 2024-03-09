from datetime import datetime
# Define Flipkart sale data
flipkart_sales = {
    'Big Saving Days': {
        'Expected Date': 'March 11th to March 15th',
        'Sale Theme': 'Best offers and discounts on mobile, electronics, TVs, appliances, home furnishing, etc.'
    },
    'Appliances Bonanza': {
        'Expected Date': 'March 16th to March 21st',
        'Sale Theme': 'Offers and discounts on home appliances.'
    },
    'Summer Sale': {
        'Expected Date': 'March 22nd to March 26th',
        'Sale Theme': 'Offers and deals on ACs, coolers, fans and more.'
    },
    'Big Bachat Dhamaal Sale': {
        'Expected Date': 'April 1st to April 3rd',
        'Sale Theme': 'Offers on electronics, discounts on smartphones, TVs, laptops, and more. Deals on fashion, home appliances, home furnishing, home decor and more.'
    },
    'Summer Saver Days': {
        'Expected Date': 'April 13th to April 17th',
        'Sale Theme': 'Offers and discounts on ACs, coolers, fans and more.'
    },
    'Electronics Sale': {
        'Expected Date': 'May 23rd to May 31st',
        'Sale Theme': 'Best offers on electronics, TVs, laptops, smartphones and more.'
    },
    'End-of-Season Sale': {
        'Expected Date': 'June 1st to June 6th',
        'Sale Theme': 'Great offers on fashion. 50-80% off on clothing and footwear.'
    },
    'Big Saving Days': {
        'Expected Date': 'June 10th to June 14th',
        'Sale Theme': 'Best offers and discounts on mobile, electronics, TVs, appliances, home furnishing, home decor, kitchen, fashion, beauty etc.'
    },
    'Grand Home Appliances Sale': {
        'Expected Date': 'June 18th to June 22nd',
        'Sale Theme': 'Good discounts on home appliances such as washing machines, refrigerators, etc.'
    },
    'Big Bachat Dhamaal Sale': {
        'Expected Date': 'June 23rd to June 25th',
        'Sale Theme': 'Offers on electronics, discounts on smartphones, TVs, laptops, fashion, home appliances, home furnishing, home decor, kitchen, beauty, toys and more.'
    },
    'Big Bachat Dhamaal Sale': {
        'Expected Date': 'July 1st to July 3rd',
        'Sale Theme': 'Offers on electronics, discounts on smartphones, TVs, laptops, fashion, home appliances, home furnishing, home decor, kitchen, beauty, toys and more.'
    },
    'Big Saving Days': {
        'Expected Date': 'July 15th to July 19th',
        'Sale Theme': 'Best offers and discounts on mobile, electronics, TVs, appliances, home furnishing, home decor, kitchen, fashion, beauty, toys, baby care, etc.'
    },
    'Flipkart Big Freedom Sale': {
        'Expected Date': 'August 5th to August 9th',
        'Sale Theme': 'Discounts and deals on smartphones, TVs, laptops, electronics, home appliances, kitchen, fashion and more.'
    },
    'Independence Day Sale': {
        'Expected Date': 'August 12th to August 15th',
        'Sale Theme': 'Offers on smartphones, electronics, home appliances, kitchen, fashion, clothing, beauty and more.'
    },
    'Flipkart TV Day Sale': {
        'Expected Date': 'August 16th to August 18th',
        'Sale Theme': 'Great offers and discounts on TVs and Smart TVs.'
    },
    'Month-End Mobile Fest': {
        'Expected Date': 'August 25th to August 31st',
        'Sale Theme': 'Offers and deals on best-selling smartphones.'
    },
    'Mega Monsoon Days Sale': {
        'Expected Date': 'August 26th to August 31st',
        'Sale Theme': 'Best offers on TV, appliances, clothing, groceries and more.'
    },
    'Grand Home Appliances Sale': {
        'Expected Date': 'September 7th to September 11th',
        'Sale Theme': 'Discounts and deals on home appliances and kitchen appliances.'
    },
    'Budget Dhamaka Sale': {
        'Expected Date': 'September 14th to September 16th',
        'Sale Theme': 'Offers on TV, appliances, fashion, groceries, kitchen appliances and more.'
    },
    'Flipkart Big Billion Day Sale': {
        'Expected Date': 'October 8th to October 15th',
        'Sale Theme': 'Biggest deals and discounts on mobiles, electronics, TVs, appliances, home furnishing, home decor, kitchen, fashion, beauty, etc.'
    },
    'Flipkart Big Dussehra Sale': {
        'Expected Date': 'October 22nd to October 29th',
        'Sale Theme': 'Offers on smartphones, TVs, electronics, laptops, tablets, home appliances, kitchen appliances, fashion and more.'
    },
    'Flipkart Big Diwali Sale': {
        'Expected Date': 'November 2nd to November 11th',
        'Sale Theme': 'On the occasion of the Diwali festive season, Flipkart offers big deals and discounts on mobiles, electronics, TVs, appliances, home furnishing, home decor, kitchen, fashion, beauty, etc.'
    },
    'Flipkart Diwali Dhamaka Sale': {
        'Expected Date': 'November 12th to November 15th',
        'Sale Theme': 'Offers on smartphones, electronics, home appliances, kitchen, fashion, clothing, beauty and more.'
    },
    'Black Friday Sale': {
        'Expected Date': 'November 27th to November 30th',
        'Sale Theme': 'Sale on multiple categories on the occasion of Black Friday.'
    },
    'Big Bachaat Sale': {
        'Expected Date': 'December 1st to December 3rd',
        'Sale Theme': 'Great discounts and offers on electronics, smartphones, TVs, appliances, fashion and more.'
    },
    'Big Saving Days': {
        'Expected Date': 'December 16th to December 21st',
        'Sale Theme': 'Best offers and discounts on mobile, electronics, TVs, appliances, home furnishing, etc.'
    },
    'Grand Gadget Days Sale': {
        'Expected Date': 'December 29th to December 31st',
        'Sale Theme': 'Biggest deals on smartphones, TWS, audio, electronics, TVs, and more.'
    },
    'Flipkart Year-End Sale': {
        'Expected Date': 'December 24th to December 31st',
        'Sale Theme': 'Best deals on multiple categories such as electronics, smartphones, TVs, tablets, fashion, kitchen, etc.'
    }
}

# Define Amazon sale data
amazon_sales = {
    'Amazon Great RepublicDay Sale': {
        'Expected Dates': 'January 14th to January 18th',
        'Product categories': 'Electronic devices, home, kitchen, and appliance',
        'Discounts': '60% off plus 10% on SBI credit card swipes'
    },
    'Grand Gaming Days': {
        'Expected Dates': 'January 8th to January 30th',
        'Product categories': 'Gaming gadgets',
        'Discounts': '60% off'
    },
    'Valentine’s Day Store': {
        'Expected Dates': 'February 2th to February 14th',
        'Product categories': 'Tech Products',
        'Discounts': 'Up to 70% off'
    },
    'Amazon Fab Phone Fest': {
        'Expected Dates': 'February 22th to February 25th',
        'Product categories': 'Various categories',
        'Discounts': '40% off + 10% cash back on big brands'
    },
    'Super Value Days offer': {
        'Expected Dates': 'March 1st to March 7th',
        'Product categories': 'Everyday supplies and groceries',
        'Discounts': '10% off'
    },
    'Amazon Holi Sale': {
        'Expected Dates': 'March 5th to March 9th',
        'Product categories': 'Fashion, beauty, appliances, etc.',
        'Discounts': 'Various deals and offers: SBI bank cards offer'
    },
    'Amazon Summer Offer': {
        'Expected Dates': 'May 4th to May 8th',
        'Product categories': 'Various categories',
        'Discounts': 'Up to 50% off, additional bank offers'
    },
    'Great Indian Summer Sale': {
        'Expected Dates': 'May 13th to May 17th',
        'Product categories': 'Electronic items',
        'Discounts': 'Up to 70% off'
    },
    'Prime Day Sale': {
        'Expected Dates': 'July 26th to July 27th',
        'Product categories': 'Several categories',
        'Discounts': 'Various discounts and deals'
    },
    'Great Freedom Fest': {
        'Expected Dates': 'August 5th to August 9th',
        'Product categories': 'All categories',
        'Discounts': 'Up to 80 % + additional 10% off'
    },
    'Amazon Black Friday Sale': {
        'Expected Dates': 'November 22nd to November 25th',
        'Product categories': 'Fashion, electronics, etc.',
        'Discounts': 'Great discounts'
    },
    'Christmas Offer': {
        'Expected Dates': 'December 21st to December 25th',
        'Product categories': 'Winter wear',
        'Discounts': 'Discounts and offers'
    }
}

# Create a nested dictionary for both Flipkart and Amazon
sales_data = {
    'flipkart': flipkart_sales,
    'amazon': amazon_sales
}

# Function to parse date strings and remove suffixes (e.g., 'th', 'st', 'nd', 'rd')
def parse_date(date_str):
    return datetime.strptime(date_str.replace('th', '').replace('st', '').replace('nd', '').replace('rd', ''), '%B %d')

# Function to find the closest approaching sale for Flipkart
def closest_sale(sales, month):
    closest_sale = min(sales.keys(), key=lambda x: abs((parse_date(sales[x]['Expected Date'].split(' to ')[0]) - parse_date(month)).days))
    return closest_sale

# Example usage:
current_month = 'August'  # Change this to the desired month
closest_flipkart_sale = closest_sale(flipkart_sales, current_month)
closest_amazon_sale = closest_sale(amazon_sales, current_month)

print("Next upcoming sale on Flipkart in", current_month, ":", closest_flipkart_sale)
print("Next upcoming sale on Amazon in", current_month, ":", closest_amazon_sale)