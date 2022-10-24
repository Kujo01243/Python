import requests

url = "https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=a46716a76c270dcc6f0ad9968d7c2eb9"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
