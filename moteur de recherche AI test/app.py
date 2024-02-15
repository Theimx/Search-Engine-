from flask import Flask, request, render_template
import sqlite3
from tfidf import tfidf

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