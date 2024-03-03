# IMPORTS
import sqlite3
from random import randint
from datetime import datetime

# VARIABLES AND OBJECTS

query = """INSERT INTO stue (datetime, temperature, humidity) VALUES(?, ?, ?)"""
data = (datetime.now(), randint(0, 30), randint(0, 100))

try:
    conn = sqlite3.connect('database/sensor_data.db')
    cur = conn.cursor()
    cur.execute(query, data)
    conn.commit()
except sqlite3.Error as sqlite_e:
    print(f'SQLite error occured')
    conn.rollback()
except Exception as e:
    print(f'Error occured')
finally:
    conn.close()