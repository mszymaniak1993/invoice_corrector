import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS invoice (id INTEGER PRIMARY KEY, invoice_number, is_created INTEGER, is_downloaded INTEGER)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM invoice WHERE is_created = 0")
        rows = self.cur.fetchall()
        return rows

    def insert(self, invoice_number):
        self.cur.execute("INSERT INTO invoice VALUES (NULL, ?, 0, 0)", (invoice_number,))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM invoice WHERE id=?", (id,))
        self.conn.commit()
    
    def edit(self, id, invoice_number):
        self.cur.execute("UPDATE invoice SET invoice_number=? WHERE id=?", (invoice_number, id))
        self.conn.commit()

    def created(self, id):
        self.cur.execute("UPDATE invoice SET is_created=1  WHERE id=?", (id,))
        self.conn.commit()

    def downloaded(self, id):
        self.cur.execute("UPDATE invoice SET is_downloaded=1  WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
