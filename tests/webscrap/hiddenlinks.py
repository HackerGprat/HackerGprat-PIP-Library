import requests as req
from bs4 import BeautifulSoup as bs

url = "https://youtube.com"

html = req.get(url)
page = bs(html.text, "html.parser")

# print(page.text)

atag = page.find_all('a')

with open("ExtractedLink.txt","w") as f:
    for tag in atag:
        f.write(tag.get("href"))
        f.write("\n") 
