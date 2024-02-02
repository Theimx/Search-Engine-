import requests
from bs4 import BeautifulSoup
URL = "https://info.blaisepascal.fr/gerer-une-base-de-donnees-avec-python/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

titles0 = soup.find_all("title")
for title0 in titles0:
  print(title0)

titles1 = soup.find_all("h1")
for title1 in titles1:
  print(title1)

titles2 = soup.find_all("h2")
for title2 in titles2:
  print(title2)

hp = soup.find_all("a")
for hp1 in hp:
  print(hp1)
