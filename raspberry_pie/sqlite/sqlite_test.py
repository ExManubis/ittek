# IMPORTS
import sqlite3, Adafruit_DHT, sys, datetime
import datetime as d
from time import sleep

# VARIABLES + OBJECTS
## DHT11
sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

## SQL
con = sqlite3.connect('test.db') # connection object
create_table = "CREATE TABLE if not exists DHT11 ( ID INTEGER PRIMARY KEY AUTOINCREMENT, datetime TEXT NOT NULL, temperature REAL NOT NULL, humidity REAL NOT NULL)"
insert_dt = "INSERT INTO DHT11 (datetime, temperature, humidity) VALUES(?,?,?)"

# PROGRAM
while True:
    try:
        cursor = con.cursor() # cursor object
        cursor.execute(create_table)
        date = d.datetime.now()
        datetime = date.strftime('%d-%m-%Y %H:%M:%S')
        data = (datetime, temperature, humidity)
        cursor.execute(insert_dt, data)
        rowid = cursor.lastrowid
        print(f'id of last row inser = {rowid}')
        print(humidity, temperature)
        con.commit()
        sleep(10)
    except sqlite3.Error as e:
        print(f'Error calling SQL: "{e}"') 
    except sqlite3.OperationalError as oe:
        print(f'Transaction could not be processed : { oe }')
    except sqlite3.IntegrityError as ie:
        print(f'Integrity constraint violated : { ie }')
    except sqlite3.ProgrammingError as pe:
        print(f'You used the wrong SQL table : { pe }')
    except KeyboardInterrupt:
        print('\nclosing...')
        con.close() # close connection
        sys.exit() # exit programme