import requests
from bs4 import BeautifulSoup
URL = "https://movies2watch.to/watch-movie/watch-spider-man-into-the-spider-verse-sequel-full-66674.9653188"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

elementsToFind = ["title","h1","h2"]
link = "a"
urlOnThePage = []
result = []

x = soup.find_all(elementsToFind[0])
for y in x:
  result.append(y)

