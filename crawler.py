import requests
from bs4 import BeautifulSoup
import sqlite3
from DataBase import create_database, remove_duplicates

def extraire_liens_et_sauvegarder(liens_a_crawler, conn):
    for url in liens_a_crawler:
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            content_length = int(response.headers["Content-Length"])
            # Vérifier si la taille du contenu est inférieure à 500 Mo (500 * 1024 * 1024 octets)
            if content_length < 500 * 1024 * 1024:
                soup = BeautifulSoup(response.text, 'html.parser')
                liens = soup.find_all('a')
                cursor = conn.cursor()
                for lien in liens:
                    href = lien.get('href')
                    if href and href.startswith('http'):
                        cursor.execute("INSERT OR IGNORE INTO liens (url) VALUES (?)", (href,))
                conn.commit()
                cursor.close()
            else:
                print(f"La taille de la page {url} est supérieure à 500 Mo. La page ne sera pas téléchargée.")
        else:
            print(f"Échec de la requête pour la page {url}. Code d'état : {response.status_code}")

#--------------------------------------------------------------------------------------------
liens_a_crawler = ['https://42.fr/', 'https://example.com']  # Ajoutez les liens que vous souhaitez crawler ici

create_database()
conn = sqlite3.connect('liens.db')
extraire_liens_et_sauvegarder(liens_a_crawler, conn)
remove_duplicates()

conn.close()
