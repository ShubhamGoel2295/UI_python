import sqlite3

class Database:
    def __init__(self):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute("create table if not exists book (id integer primary key, title text, author text, year integer, isbn integer)")
        conn.commit()
        conn.close()

    def view(self):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute("select * from book")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self, title='', author='', year='', isbn=''):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute("select * from book where title=? or author =? or year=? or isbn=?", (title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows

    def insert(self, title, author, year, isbn):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute("insert into book values(Null, ?, ?, ?, ?)", (title, author, year, isbn))
        conn.commit()
        conn.close()

    def delete(self, id):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute("delete from book where id=?", (id,))
        conn.commit()
        conn.close()

    def update(self, id, title, author, year, isbn):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute("update book set title=?, author=?, year=?, isbn=? where id=?", (title, author, year, isbn, id))
        conn.commit()
        conn.close()
# connect()
# insert('The Moon', 'Don swizh', 1940, 154447)
# print(search(author='John Smith'))
# print(view())