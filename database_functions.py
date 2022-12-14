

#sqllite3 imported through databaseconnection
import databaseconnection as db
import sqlite3

def show_table(tablename, fancy_print = False):
    if not fancy_print: 
        try:
            # Write a query and execute it with cursor
            # Fetch and output resul
            query = 'select * from ' + tablename + ";"
            count = db.cursor.execute(query)
            result = db.cursor.fetchall()
        
            if len(result) == 0:
                print('lege tabel!')
            else:
                return result
        except sqlite3.Error as error:
            print('Error occured - ', error)
    elif fancy_print:
        for index in range(number_of_records(tablename)):
            print(show_record(tablename, index, True))

def show_record(tablename, id, Fancyprint = False):

    try:
        # Write a query and execute it with cursor
        # Fetch and output resul
        query = 'select * from ' + tablename + ' id =' + str(id) +";"
        count = db.cursor.execute(query)
        result = db.cursor.fetchall()
    
        if len(result) == 0:
            print('lege tabel!')
        else:
            if not Fancyprint: 
                return result
            #elif Fancyprint:
             #   string_print = ''
              #  for index in range(number_of_columns(tablename)):
               #     string_print += str(result[index[0]]).ljust(20)
                #return string_print

    except sqlite3.Error as error:
        print('Error occured - ', error)



def show_field(tablename, id, fieldname):
    try:
        # Write a query and execute it with cursor
        # Fetch and output resul
        query = 'select ' + fieldname + ' from ' + tablename + ' where id =' + str(id) +";"
        count = db.cursor.execute(query)
        result = db.cursor.fetchall()
    
        if len(result) == 0:
            print('lege tabel!')
        else:
            return result[0][0]
    except sqlite3.Error as error:
        print('Error occured - ', error)



def number_of_records(tablename):
    list_records = show_table(tablename)
    return len(list_records)

def number_of_columns(tablename):
    record = show_table(tablename)
    return len(record)

    
def delete_record(tablename, id):
    try:
        query = 'delete from ' + tablename + ' where id =' + str(id) +";"
        count = db.cursor.execute(query)
        result = db.cursor.commit()

    except Exception as e:
        print('delete_record error: {} '.format(e))


def delete_fieldname(tablename, id, fieldname):
    try:
        query = 'delete ' + fieldname + ' from ' + tablename + ' where id =' + str(id) +";"
        count = db.cursor.execute(query)
        result = db.cursor.commit()
    
        if len(result) == 0:
            print('lege tabel!')
        else:
            return result[0][0]
    except sqlite3.Error as error:
        print('Error occured - ', error)


