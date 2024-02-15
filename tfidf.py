import sqlite3
import math

def tfidf(termes_recherches, corpus):
    tf = {}
    idf = {}
    tfidf_score = {}

    # Calculer le TF pour chaque terme dans chaque document
    for document in corpus:
        tf[document['url']] = {}
        total_mots = len(document['texte'].split())
        
        # Vérifier si le texte n'est pas vide pour éviter la division par zéro
        if total_mots > 0:
            for terme in termes_recherches:
                tf[document['url']][terme] = document['texte'].count(terme) / total_mots

    # Calculer l'IDF pour chaque terme
    total_documents = len(corpus)
    for terme in termes_recherches:
        document_occurrences = sum(1 for document in corpus if terme in document['texte'])
        idf[terme] = math.log(total_documents / (document_occurrences + 1))

    # Calculer le score TF-IDF pour chaque terme dans chaque document
    for url, termes_tf in tf.items():
        tfidf_score[url] = {}
        for terme, tf_value in termes_tf.items():
            tfidf_score[url][terme] = tf_value * idf[terme]

    return tfidf_score

def afficher_resultats(scores_tfidf):
    for document, scores in scores_tfidf.items():
        print(f"URL: {document}")
        for terme, score in scores.items():
            print(f"  - Terme: {terme}, Score TF-IDF: {score}")
        print()

if __name__ == "__main__":
    # Connexion à la base de données SQLite3
    conn = sqlite3.connect('liens.db')

    # Récupération de tous les documents de la base de données
    cursor = conn.cursor()
    cursor.execute("SELECT url, texte FROM contenu_pages")
    corpus = [{'url': row[0], 'texte': row[1]} for row in cursor.fetchall()]
    cursor.close()

    # Termes à rechercher
    termes_recherches = ['python', 'data', 'analyse']

    # Calcul des scores TF-IDF
    scores_tfidf = tfidf(termes_recherches, corpus)

    # Affichage des résultats
    afficher_resultats(scores_tfidf)

    # Fermeture de la connexion à la base de données
    conn.close()