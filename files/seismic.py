import requests

token = "xxxx"
url = "https://api.seismic.com/reporting/v2/contents?limit=1"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

print(response.text)