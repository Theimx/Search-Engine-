from flask import Flask, render_template, request
import sqlite3
import webbrowser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form['keyword']
        conn = sqlite3.connect('links.db')
        c = conn.cursor()
        c.execute("SELECT url FROM links WHERE url LIKE ?", ('%' + keyword + '%',))
        results = c.fetchall()
        conn.close()
        return render_template('results.html', keyword=keyword, results=results)
    return render_template('index.html')

if __name__ == '__main__':
    # Création de la base de données SQLite si elle n'existe pas
    conn = sqlite3.connect('links.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS links (id INTEGER PRIMARY KEY, url TEXT)''')
    conn.commit()
    conn.close()
    
    # Ouvrir le navigateur web avec l'application Flask
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True)