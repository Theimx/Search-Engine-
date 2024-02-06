import requests
from bs4 import BeautifulSoup

def extraire_informations(url):

    liste_liens = []
    liste_titres = []
    liste_sous_titres = []

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        liens = soup.find_all('a')

        for lien in liens:
            href = lien.get('href')
            if href and href.startswith('http'):
                liste_liens.append(href)

        titres = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

        for titre in titres:
            liste_titres.append(titre.text.strip())

        sous_titres = soup.find_all(['h2', 'h3', 'h4', 'h5', 'h6'])

        for sous_titre in sous_titres:
            liste_sous_titres.append(sous_titre.text.strip())

        return liste_liens, liste_titres, liste_sous_titres
    else:
        print(f"Échec de la requête. Code d'état : {response.status_code}")
        return None, None, None

#---------------------------------------------------------------------------------------------
url = 'https://numpy.org/'
liens, titres, sous_titres = extraire_informations(url)

for lien in liens:
    print(lien)
for titre in titres:
    print(titre)
for sous_titre in sous_titres:
    print(sous_titre)
