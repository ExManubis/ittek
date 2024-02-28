# IMPORTS
import sqlite3
from datetime import datetime
from random import randint
from time import sleep

# FUNCTIONS
def log_kontor_dht11():
    while True:
        query = """
        INSERT INTO kontor (datetime, temperature, humidity) VALUES(?,?,?)
        """
        data = (datetime.now(), randint(0, 30), randint(0, 100))
        try:
            conn = sqlite3.connect("database/sensor_data.db")
            cur = conn.cursor()
            cur.execute(query, data)
            conn.commit()    
        except sqlite3.Error as sql_e:
            print(f"SQLite error occured: {sql_e}")
            conn.rollback()
        except Exception as e:
            print(f"Error occured: {e}")
        finally:
            conn.close()
        sleep(2)

# SCRIPT
log_kontor_dht11()