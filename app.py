from flask import Flask, request, render_template
import sqlite3
from tfidf import tfidf
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

def connect_database():
    return sqlite3.connect('liens.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rechercher')
def rechercher():
    # Connexion à la base de données
    conn = connect_database()

    # Récupérer la requête de recherche depuis l'URL
    query = request.args.get('query')

    # Récupérer tous les documents de la base de données
    cursor = conn.cursor()
    cursor.execute("SELECT url, texte FROM contenu_pages")
    corpus = [{'url': row[0], 'texte': row[1]} for row in cursor.fetchall()]
    cursor.close()

    # Termes à rechercher
    termes_recherches = query.split()  # Diviser la requête en termes individuels

    # Calcul des scores TF-IDF
    scores_tfidf = tfidf(termes_recherches, corpus)

    # Fermeture de la connexion à la base de données
    conn.close()

    # Affichage des résultats
    return render_template('resultats.html', query=query, scores_tfidf=scores_tfidf)

if __name__ == "__main__":
    # Créer la base de données si elle n'existe pas
    from DataBase import create_database
    create_database()

    # Lancer l'application Flask
    app.run(debug=True)

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

        # Vérifier si le texte n'est pas vide
        if texte:
            # Insérer les données dans la nouvelle table
            cursor.execute("INSERT INTO contenu_pages (url, titre, sous_titre, texte) VALUES (?, ?, ?, ?)",
                           (url, titre, sous_titre, texte))
            conn.commit()
            print(f"Données insérées pour l'URL {url}")
        else:
            print(f"Aucun contenu trouvé pour l'URL {url}.")
    else:
        print(f"Échec de la requête pour l'URL {url}. Code d'état : {response.status_code}")

    # Fermeture du curseur
    cursor.close()