import requests

token = "xxxxx"

url = "https://api.seismic.com/search/v1/content/query?"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

search_term = "Envizi-Integration-Hub-Webinar",

# Request payload
payload = {
    "term": f"{search_term}",
    "options":{ 
            "searchFields":["name","properties"],
            "returnFields":["id", "name", "type", "downloadUrl", "applicationUrls"]
            },
    "pageSize": 10  # Number of results to return
}

response = requests.post(url, headers=headers, json=payload)

print(response.text)
