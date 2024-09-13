import requests

a = requests.get("https://www.google.com")
print(a.text)