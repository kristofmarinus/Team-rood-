schemaname = 'rooddb.db'
#tablename = 'tasks'
cursor = None
sqliteConnection = None
import sqlite3


def make_connection():
    global sqliteConnection
    global cursor
    try:
        sqliteConnection = sqlite3.connect(schemaname) # Connect to DB and create a cursor
        cursor = sqliteConnection.cursor()

    except sqlite3.Error as error:
        print('Error occured - ', error)

'''def commint():
    pass'''


make_connection()
print('connection db made')