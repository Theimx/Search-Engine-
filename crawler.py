import requests
from bs4 import BeautifulSoup

Web=requests.get("https://www.google.com/")
soup=BeautifulSoup(Web.text,'lxml')
for link in soup.findAll('a'):
    print(link['href'])
