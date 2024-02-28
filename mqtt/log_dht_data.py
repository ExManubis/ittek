# IMPORTS
import sqlite3
from random import randint

# Connection
try:
    conn = sqlite3.connect("database/sensor_data.db")
    cur = conn.cursor()    
except sqlite3.Error as sql_e:
    print(f"SQLite error occured: {sql_e}")
    conn.rollback()
except Exception as e:
    print(f"Error occured: {e}")
finally:
    conn.close()