import requests
from bs4 import BeautifulSoup

def extraire_liens(url):

    liste_liens = []
    response = requests.get(url)

    if response.status_code == 200:
        
        soup = BeautifulSoup(response.text, 'html.parser')
        liens = soup.find_all('a')

        for lien in liens:
            href = lien.get('href')
            if href and href.startswith('http'):
                liste_liens.append(href)

        return liste_liens
    else:
        print(f"Échec de la requête. Code d'état : {response.status_code}")
        return None

#-----------------------------------------------------
url = 'https://numpy.org/'
liens_trouves = extraire_liens(url)


for lien in liens_trouves:
    print(lien)
