import requests
from bs4 import BeautifulSoup
URL = "https://movies2watch.to/watch-movie/watch-spider-man-into-the-spider-verse-sequel-full-66674.9653188"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

urlOnThePage = []
result = []
elementsToFind = ["title","h1","h2"]
cliquableLink = "a"
searchElement = soup.find_all("a")


l = [1,2,3,4]
counter = 0
for i in l:
    print(l[counter])
    counter += 1
counter = 0

cliquableLinkOnThePage = soup.find_all("a")
for link in cliquableLinkOnThePage:
  print(link)

print(urlOnThePage)

#-------------------------------------------------------------
import requests
from bs4 import BeautifulSoup

URL = "https://movies2watch.to/watch-movie/watch-spider-man-into-the-spider-verse-sequel-full-66674.9653188"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
titles = soup.find_all("a")
for title in titles:
  print(title)

print("""

""")
print('Voici les titres h1')
titles_1 = soup.find_all('h1')
for title in titles_1:
  indice=title.text.find('[')
  print(title.text[:indice])

print("""

""")
print('Voici les titres h2')
titles_2 = soup.find_all('h2')
for title in titles_2:
  indice=title.text.find('[')
  print(title.text[:indice])

print("""

""")
print('Voici les titres h3') 
titles_3 = soup.find_all('h3')
for title in titles_3:
  indice=title.text.find('[')
  print(title.text[:indice])

#----------------------------------------------
  
import requests
from bs4 import BeautifulSoup

url = "https://42.fr/apres-42/"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    print(link.get('href'))
