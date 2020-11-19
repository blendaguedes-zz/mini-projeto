import sqlite3

conn = sqlite3.connect("exemplo.sqlite")

cursor = conn.cursor()


def create_table():
    query = "CREATE TABLE exemplo( id INTEGER PRIMARY KEY AUTOINCREMENT, coluna1 TEXT)"

    cursor.execute(query)


def insert_data(id, nome):
    conn = sqlite3.connect("exemplo.sqlite")

    cursor = conn.cursor()

    query = "INSERT INTO exemplo values (?, ?)"
    cursor.execute(query, (id, nome))
    conn.commit()


# def insert_data(values):
#     query = "INSERT INTO exemplo values (?, ?)"
#     cursor.execute(query, values)
#     conn.commit()
def get_data():
    cursor = conn.cursor()
    query = "SELECT * FROM exemplo"
    all_data = cursor.execute(query).fetchall()
    return all_data
