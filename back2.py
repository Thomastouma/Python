import mysql.connector


# Connecting to database toumatest, executing sql code that inserts new data into the database.
def insert(title, author, year):
    conn = mysql.connector.connect(host='localhost', user='root', passwd='root', db='toumatest')
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,%s, %s, %s)", (title, author, year))
    conn.commit()
    conn.close()

# Connecting to database toumatest, executing sql code into the database that gather all the data and displays it
def view():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='root', db='toumatest')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

# Connecting to database toumatest, executing sql code into the database that deletes all the data where id equals input
def delete(id):
    conn = mysql.connector.connect(host='localhost', user='root', passwd='root', db='toumatest')
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=%s", (id,))
    conn.commit()
    conn.close()

# Connecting to database toumatest, executing sql code into the database that updates the data at chosen id
def update(id, title, author, year):
    conn = mysql.connector.connect(host='localhost', user='root', passwd='root', db='toumatest')
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=%s, author=%s, year=%s WHERE id=%s", (title, author, year, id))
    conn.commit()
    conn.close()

