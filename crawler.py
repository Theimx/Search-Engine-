import requests
from bs4 import BeautifulSoup
URL = "https://datascientest.com/sql-tout-savoir#:~:text=SQL%20ou%20%C2%AB%20Structured%20Query%20Language,les%20donn%C3%A9es%20qu'elles%20contiennent."
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
titles = soup.find_all("h1")
for title in titles:
  print(title)