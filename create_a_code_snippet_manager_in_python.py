# Use sqlite3 for a simple code snippet manager
import sqlite3
conn = sqlite3.connect('code_snippets.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS snippets
             (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, code TEXT)''')
def add_snippet(title, code):
    c.execute("INSERT INTO snippets (title, code) VALUES (?, ?)", (title, code))
    conn.commit()
def get_all_snippets():
    c.execute("SELECT * FROM snippets")
    return c.fetchall()
def search_snippet(title):
    c.execute("SELECT * FROM snippets WHERE title=?", (title,))
    return c.fetchall()
def update_snippet(id, title, code):
    c.execute("UPDATE snippets SET title=?, code=? WHERE id=?", (title, code, id))
    conn.commit()
def delete_snippet(id):
    c.execute("DELETE FROM snippets WHERE id=?", (id,))
    conn.commit()
conn.close() # remember to close the connection when done.
# Please Like and Subscribe