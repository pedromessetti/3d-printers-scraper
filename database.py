import sqlite3

def table_exists(table_name):
    try:
        conn = sqlite3.connect("printers.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        result = cursor.fetchone()
        conn.close()
        if result:
            return True
        else:
            return False
    except sqlite3.Error as error:
        print("Error checking if the table exists in sqlite\n", error)


def create_table():
    try:
        conn = sqlite3.connect("printers.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS printers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price TEXT, timestamp TEXT, status TEXT DEFAULT '1', website TEXT)")
        conn.commit()
        conn.close()
        print("Table created successfully")
    except sqlite3.Error as error:
        print("Error creating the table in sqlite\n", error)


def save_data(data):
    try:
        conn = sqlite3.connect("printers.db")
        cursor = conn.cursor()

        # Insert data into the table
        cursor.executemany("INSERT INTO printers (name, price, timestamp, website) VALUES (?, ?, ?, ?)", data)

        conn.commit()
        conn.close()

        print("Data saved to database.")
    except sqlite3.Error as error:
        print("Error inserting data\n", error)