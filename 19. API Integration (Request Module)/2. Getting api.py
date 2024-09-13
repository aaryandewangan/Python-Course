#getting an API

import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
  "id": 101,
  "title": 'Aaryan',
  "body": 'bar',
  "userId": 1
}

headers = {
    'Content-type': 'application/json; charset=UTF-8',
  }

a = requests.post(url, headers=headers, json=data)
print(a.text)

#bs4 is a package which simplifies the HTML requests

url2 = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"

b = requests.get(url2)

from bs4 import BeautifulSoup
soup = BeautifulSoup(b.text, 'html.parser')
print(soup.prettify())

print("Printing all Heading which are h2 - ")
for heading in soup.find_all("h2"):
    print(heading.text)