import requests
import json

query = input("What type of news are you Interested in ?: ")
api_key = "2f63b9bbf1a34adaad30bafcd51da24f" 
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-07-30&sortBy=publishedAt&apiKey={api_key}"
response = requests.get(url)

news = json.loads(response.text)
for article in news["articles"]:
    print(f"Title: {article["title"]}")
    print(f"Description: {article["description"]}")
    print("----------------------------")  