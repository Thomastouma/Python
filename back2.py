import mysql.connector


# Connecting to database toumatest, executing sql code that inserts new data into the database.
def insert(datum, timmar, butiker, miltal):
    conn = mysql.connector.connect(host='localhost', user='root', passwd='root', db='tidrapportering')
    cur = conn.cursor()
    cur.execute("INSERT INTO gottmix VALUES (NULL,%s, %s, %s, %s)",
                (datum, timmar, butiker, miltal))  # Takes users input and store it
    # in the database
    conn.commit()
    conn.close()  # Closes the connection


# Connecting to database tidrapporteing, executing sql code into the database that gather all the data and displays it
def view():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='root', db='tidrapportering')
    cur = conn.cursor()
    cur.execute("SELECT * FROM gottmix")  # Selects all data from the database table book
    rows = cur.fetchall()
    conn.close()  # Closes the connection
    return rows  # returns the data so it can be used


def extract_excel_data():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='root', db='tidrapportering')
    cur = conn.cursor()
    cur.execute("SELECT datum, timmar FROM gottmix")  # Selects all data from the database table book
    excel_data = cur.fetchall()
    conn.close()  # Closes the connection
    return excel_data  # returns the data so it can be used


# Connecting to database toumatest, executing sql code into the database that deletes all the data where id equals input
def delete(id):
    conn = mysql.connector.connect(host='localhost', user='root', passwd='root', db='tidrapportering')
    cur = conn.cursor()
    cur.execute("DELETE FROM gottmix WHERE id=%s", (id,))  # Deleting data by choosing where id is equal to input
    conn.commit()
    conn.close()  # Closes the connection


# Connecting to database toumatest, executing sql code into the database that updates the data at chosen id
def update(id, datum, timmar, butiker, miltal):
    conn = mysql.connector.connect(host='localhost', user='root', passwd='root', db='tidrapportering')
    cur = conn.cursor()
    cur.execute("UPDATE gottmix SET datum=%s, timmar=%s, butiker=%s, miltal=%s WHERE id=%s", (datum, timmar, butiker, miltal, id))
    conn.commit()
    conn.close()  # Closes the connection
