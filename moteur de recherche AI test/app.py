from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('links.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS links (id INTEGER PRIMARY KEY, url TEXT)''')
conn.commit()
conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form['keyword']
        # Traiter la recherche ici
        return render_template('results.html', keyword=keyword)
    return render_template('index.html')

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
    app.run(debug=True)