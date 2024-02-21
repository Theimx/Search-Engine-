import requests
from bs4 import BeautifulSoup
import sqlite3
from DataBase import create_database, remove_duplicates

def extraire_liens_et_sauvegarder(liens_a_crawler, conn):
    for url in liens_a_crawler:
        response = requests.get(url)

        if response.status_code == 200:
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
            print(f"Échec de la requête pour la page {url}. Code d'état : {response.status_code}")

#--------------------------------------------------------------------------------------------
liens_a_crawler = []  # Ajoutez les liens que vous souhaitez crawler ici

create_database()
conn = sqlite3.connect('liens.db')
extraire_liens_et_sauvegarder(liens_a_crawler, conn)
remove_duplicates()

conn.close()