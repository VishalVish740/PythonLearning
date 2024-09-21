import json
import requests

url = "https://google.com"
response = requests.get(url)
print(response)

# Importing Api 
import requests
import json
query = input("What type of News want to see:")
# url = f"https://newsapi.org/v2/everything?q={query}&from=2023-12-12&sortBy=publishedAt&apiKey=dbe57b028aeb41e285a226a94865f7a7"
url = f"https://newsapi.org/v2/everything?q={query}&apiKey=df4542e0c22f419199aa9502a56cf3f5"
req = requests.get(url)
# print(req.text)
news = json.loads(req.text)
# print(news,(type(news)))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------------------------------")