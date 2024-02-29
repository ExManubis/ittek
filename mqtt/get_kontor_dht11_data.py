# IMPORTS
import sqlite3
from datetime import datetime
from random import randint
from time import sleep

# FUNCTIONS
def get_kontor_data(number_of_rows):
    query = """
    SELECT * FROM kontor;
    """
    datetimes = []
    temperatures = []
    humidities = []
    try:
        conn = sqlite3.connect("database/sensor_data.db")
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchmany(number_of_rows)
        for row in rows:
            datetimes.append(row[1])
            temperatures.append(row[2])
            humidities.append(row[3])
        return datetimes, temperatures, humidities
    except sqlite3.Error as sql_e:
        print(f"SQLite error occured: {sql_e}")
        conn.rollback()
    except Exception as e:
        print(f"Error occured: {e}")
    finally:
        conn.close()
    sleep(2)

# SCRIPT
get_kontor_data(10)