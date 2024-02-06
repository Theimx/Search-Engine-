import sqlite3

def create_database():

    conn = sqlite3.connect('liens.db')

    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS liens
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       url TEXT)''')
    conn.commit()
    cursor.close()
    conn.close()

def clear_table():

    conn = sqlite3.connect('liens.db')

    cursor = conn.cursor()
    cursor.execute("DELETE FROM liens")
    conn.commit()
    cursor.close()

    conn.close()

def remove_duplicates():

    conn = sqlite3.connect('liens.db')

    cursor = conn.cursor()
    cursor.execute("DELETE FROM liens WHERE id NOT IN (SELECT MIN(id) FROM liens GROUP BY url)")
    conn.commit()
    cursor.close()

    conn.close()

def detecter_et_supprimer_doublons():

    conn = sqlite3.connect('liens.db')

    cursor1 = conn.cursor()
    cursor2 = conn.cursor()

    cursor1.execute("SELECT id, url FROM liens")
    rows = cursor1.fetchall()

    for row1 in rows:
        id1, url1 = row1
        cursor2.execute("SELECT id FROM liens WHERE url=? AND id < ?", (url1, id1))
        duplicates = cursor2.fetchall()

        for duplicate in duplicates:
            id_duplicate = duplicate[0]
            cursor2.execute("DELETE FROM liens WHERE id=?", (id_duplicate,))
            print(f"Suppression du doublon avec l'ID {id_duplicate}")

    conn.commit()
    cursor1.close()
    cursor2.close()
    conn.close()

if __name__ == "__main__":
    detecter_et_supprimer_doublons()

if __name__ == "__main__":
    create_database()
