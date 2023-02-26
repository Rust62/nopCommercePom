import requests

url = "https://admin-demo.nopcommerce.com/lib_npm/cldr-data/supplemental/weekData.json"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.headers)
print(response.content)
print(response.json())


assert response.status_code == 200

