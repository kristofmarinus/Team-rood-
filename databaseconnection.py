schemaname = 'rooddb.db'
tablename = 'tasks'
cursor = None
sqliteConnection = None

import sqlite3
from list_task import show_all_tasks

def make_connection():
    global sqliteConnection
    global cursor
    try:
        sqliteConnection = sqlite3.connect(schemaname) # Connect to DB and create a cursor
        cursor = sqliteConnection.cursor()
    except sqlite3.Error as error:
        print('Error occured - ', error)


make_connection()
print('connection db made')