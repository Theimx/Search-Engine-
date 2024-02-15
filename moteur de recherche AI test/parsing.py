import sqlite3
import requests
from bs4 import BeautifulSoup
from DataBase import create_database

def create_new_table():
    # Connexion à la base de données SQLite3
    conn = sqlite3.connect('liens.db')

    # Création de la nouvelle table si elle n'existe pas
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contenu_pages
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       url TEXT,
                       titre TEXT,
                       sous_titre TEXT,
                       texte TEXT)''')
    conn.commit()
    cursor.close()

    # Fermeture de la connexion à la base de données
    conn.close()

def analyse_et_insere_contenu(url, conn):
    # Connexion à la base de données SQLite3
    cursor = conn.cursor()

    # Vérifier si l'URL existe déjà dans la deuxième table
    cursor.execute("SELECT url FROM contenu_pages WHERE url=?", (url,))
    existing_url = cursor.fetchone()
    if existing_url:
        print(f"L'URL {url} existe déjà dans la table 'contenu_pages'.")
        return

    # Récupérer le contenu de la page
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Récupérer les titres, sous-titres et texte restant de la page
        titre = soup.title.text.strip() if soup.title else ""
        sous_titre = ", ".join([h.text.strip() for h in soup.find_all(['h2', 'h3', 'h4', 'h5', 'h6'])])
        texte = '\n'.join(filter(lambda x: x.strip(), soup.stripped_strings))  # Supprimer les lignes vides
       
        # Insérer les données dans la nouvelle table
        cursor.execute("INSERT INTO contenu_pages (url, titre, sous_titre, texte) VALUES (?, ?, ?, ?)",
                       (url, titre, sous_titre, texte))
        conn.commit()
        print(f"Données insérées pour l'URL {url}")
    else:
        print(f"Échec de la requête pour l'URL {url}. Code d'état : {response.status_code}")

    # Fermeture du curseur
    cursor.close()

if __name__ == "__main__":
    # Créer la base de données si elle n'existe pas
    create_database()

    # Créer la nouvelle table si elle n'existe pas
    create_new_table()

    # Connexion à la base de données SQLite3
    conn = sqlite3.connect('liens.db')

    # Sélectionner toutes les URLs de la première table
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM liens")
    rows = cursor.fetchall()
    cursor.close()

    # Analyser chaque URL et insérer le contenu dans la nouvelle table
    for row in rows:
        url = row[0]
        analyse_et_insere_contenu(url, conn)

    # Fermeture de la connexion à la base de données
    conn.close()