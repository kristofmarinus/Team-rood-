

#sqllite3 imported through databaseconnection
import databaseconnection as db
import sqlite3

def show_table(tablename):
    try:
        # Write a query and execute it with cursor
        # Fetch and output resul
        query = 'select * from ' + tablename + ";"
        count = db.cursor.execute(query)
        result = db.cursor.fetchall()
    
        if len(result) == 0:
            print('lege tabel!')
        else:
            print('output {}'.format(result))
    except sqlite3.Error as error:
        print('Error occured - ', error)

def show_record(tablename, id):
    try:
        # Write a query and execute it with cursor
        # Fetch and output resul
        query = 'select * from ' + tablename + ' where pk_task_id =' + str(id) +";"
        count = db.cursor.execute(query)
        result = db.cursor.fetchall()
    
        if len(result) == 0:
            print('lege tabel!')
        else:
            print('output {}'.format(result))
    except sqlite3.Error as error:
        print('Error occured - ', error)

def show_field(tablename, id, fieldname):
    try:
        # Write a query and execute it with cursor
        # Fetch and output resul
        query = 'select ' + fieldname + ' from ' + tablename + ' where pk_task_id =' + str(id) +";"
        count = db.cursor.execute(query)
        result = db.cursor.fetchall()
    
        if len(result) == 0:
            print('lege tabel!')
        else:
            return result[0][0]
    except sqlite3.Error as error:
        print('Error occured - ', error)


def delete_record():
    try:
        query = 'select * from ' + tablename + ' where pk_task_id =' + str(id) + ";"
        count = db.cursor.execute(query)

        pass

    except Exception as e:
        print('delete_record error: {} '.format(e))
    pass

def delete_field():
    pass

