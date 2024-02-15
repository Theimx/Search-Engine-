import sqlite3
import math

def tfidf(termes_recherches, corpus):
    # Calcul du TF pour chaque terme dans chaque document
    tf = {}
    for document in corpus:
        tf[document['url']] = {}
        total_mots = len(document['texte'].split())
        for terme in termes_recherches:
            tf[document['url']][terme] = document['texte'].count(terme) / total_mots

    # Calcul du IDF pour chaque terme
    idf = {}
    total_documents = len(corpus)
    for terme in termes_recherches:
        nb_documents_contenant_terme = sum(1 for document in corpus if terme in document['texte'])
        idf[terme] = math.log(total_documents / (1 + nb_documents_contenant_terme))

    # Calcul du score TF-IDF pour chaque terme dans chaque document
    scores_tfidf = {}
    for document in corpus:
        scores_tfidf[document['url']] = {}
        for terme in termes_recherches:
            scores_tfidf[document['url']][terme] = tf[document['url']][terme] * idf[terme]

    return scores_tfidf

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