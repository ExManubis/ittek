# IMPORTS
import sqlite3, datetime

# VARIABLES + OBJECTS
con = sqlite3.connect('test.db') # connection object

# PROGRAM
try:
    cursor = con.cursor() # cursor object
    cursor.execute("CREATE TABLE DATA( ID INTEGER PRIMARY KEY AUTOINCREMENT, datetime TEXT NOT NULL, temperature TEXT NOT NULL, humidity TEXT NOT NULL)")
    con.commit()
except sqlite3.Error as e:
    print(f'Error calling SQL: "{e}"') 
except sqlite3.OperationalError as oe:
    print(f'Transaction could not be processed : { oe }')
except sqlite3.IntegrityError as ie:
    print(f'Integrity constraint violated : { ie }')
except sqlite3.ProgrammingError as pe:
    print(f'You used the wrong SQL table : { pe }')
except:
    print('Some other mishap occurred')
finally:
    con.close() # close connection