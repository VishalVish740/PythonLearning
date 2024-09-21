# Day88 --> Solution
# Day89 --> Request module
import requests
# Get Request method
response = requests.get("https://google.com")
print("Printing Response", response.text)
print("Printing Cookies", response.cookies)

# POST Method
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": 'Vishal',
    "body": 'Vishwakarma',
    "UserId": 123,
}

headers = {
    'Content-type': 'application/json;charset=UTF-8',
}
'''
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Content-Type": "application/json"
}
'''
response = requests.post(url, headers=headers, json=data)
print(response.text)

# News Api Solution
# Day93--> Exercise NEWS API
import requests
import json
query = input("What type of News want to see:")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-12-12&sortBy=publishedAt&apiKey=dbe57b028aeb41e285a226a94865f7a7"
req = requests.get(url)
# print(req.text)
news = json.loads(req.text)
# print(news,(type(news)))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------------------------------")