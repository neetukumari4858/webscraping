import requests
from bs4 import BeautifulSoup
url="https://www.w3schools.com/"
req=requests.get(url)
html_content=req.content
soup=BeautifulSoup(html_content,"html.parser")
print(soup.prettify)

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)

print(soup.p)
print(soup.a)
print(soup.find_all("a"))
print(soup.find("a"))

print(soup.find(id="myAccordion"))

for link in soup.find_all("a"):
    print(link.get("href"))


for image in soup.find_all("img"):
    print(image.get('src'))


product= soup.find_all('div',class_="w3-main")
print(product)


product= soup.find('div',attrs={'class':"w3-row w3-padding-32 ws-light-green"})
print(product)



