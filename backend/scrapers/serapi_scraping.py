from serpapi import GoogleSearch

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
    for result in organic_results:
        link = result.get("link")
        if "/p/" in link or "/buy/" in link or "/proddetail" in link or "/itm" in link:
            title = result.get("title")
            print(f"{link}\n")

queries = ["Iphone 15"]
platforms = ["flipkart", "ebay", "indiamart"]

for product in queries:
    for platform in platforms:
        print(f"Results for: {platform} {product}")
        extract_search_results(product, platform)
        print("\n")
