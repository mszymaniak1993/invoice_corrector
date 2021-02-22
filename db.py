import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS invoice (id INTEGER PRIMARY KEY, invoice_number, is_created INTEGER, is_downloaded INTEGER, message)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT invoice_number FROM invoice WHERE is_created = 0")
        rows = self.cur.fetchall()
        return rows

    def insert(self, invoice_number):
        self.cur.execute("INSERT INTO invoice VALUES (NULL, ?, 0, 0, '')", (invoice_number,))
        self.conn.commit()

    def remove(self, invoice_number):
        self.cur.execute("DELETE FROM invoice WHERE invoice_number=?", (invoice_number,))
        self.conn.commit()
    
    def edit(self, invoice_number_old, invoice_number_new):
        self.cur.execute("UPDATE invoice SET invoice_number=? WHERE invoice_number=?", (invoice_number_new, invoice_number_old))
        self.conn.commit()

    def created(self, number):
        self.cur.execute("UPDATE invoice SET is_created=1 WHERE invoice_number=?", (number,))
        self.conn.commit()

    def downloaded(self, number):
        self.cur.execute("UPDATE invoice SET is_downloaded=1 WHERE invoice_number=?", (number,))
        self.conn.commit()
    """
    def message(self, invoice_number, correct_number):
        self.cur.execute("UPDATE invoice SET message='Dla faktury {} wystawiono korekte {}' WHERE invoice_number=?".format(invoice_number, correct_number), (invoice_number))
        self.conn.commit()"""

    def __del__(self):
        self.conn.close()
