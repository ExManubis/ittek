# IMPORTS
import sqlite3
from random import randint
from datetime import datetime
from time import sleep

# VARIABLES AND OBJECTS

#query = """INSERT INTO stue (datetime, temperature, humidity) VALUES(?, ?, ?)"""
#data = (datetime.now(), randint(0, 30), randint(0, 100))

# FUNCTIONS
def create_table():
    query = """CREATE TABLE IF NOT EXISTS stue(ID INTEGER PRIMARY KEY AUTOINCREMENT, datetime TEXT NOT NULL, temperature REAL NOT NULL, humidity REAL NOT NULL);"""
    try:
        conn = sqlite3.connect('database/sensor_data.db')
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
    except sqlite3.Error as sqlite_e:
        print(f'SQLite error occured')
    except Exception as e:
        print(f'Error occured')
    finally:
        conn.close()
    sleep(1)

def log_stue_dht11():
    while True:
        query = """INSERT INTO stue (datetime, temperature, humidity) VALUES(?, ?, ?)"""
        now = datetime.now()
        now = now.strftime('%d/%m/%y %H:%M:%S')
        data = (now, randint(0, 30), randint(0, 100))
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
        sleep(1)

# SCRIPT
while True:
    create_table()
    log_stue_dht11()