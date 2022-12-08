

#sqllite3 imported through databaseconnection
import databaseconnection as db

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