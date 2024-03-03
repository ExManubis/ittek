# IMPORTS
import sqlite3
from random import randint
from datetime import datetime

# FUNCTIONS
def get_stue_data(number_of_rows):
    query = """SELECT * FROM stue;"""
    datetimes = []
    temperatures = []
    humidities = []
    try:
        conn = sqlite3.connect('database/sensor_data.db')
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchmany(number_of_rows)
        for row in rows:
            datetimes.append(row[1])
            temperatures.append(row[2])
            humidities.append(row[3])
        return datetimes, temperatures, humidities
    except sqlite3.Error as sqlite_e:
        print(f'SQLite error occured')
        conn.rollback()
    except Exception as e:
        print(f'Error occured')
    finally:
        conn.close()

# SCRIPT
get_stue_data(10)