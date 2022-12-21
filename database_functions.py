

#sqllite3 imported through databaseconnection
import databaseconnection as db
import sqlite3

def give_table(tablename:str)->list:
    """returns a table from database

    Args:
        tablename (_type_): tablenames as string. for example 'tasks'
    Returns:
        _list_: list containing the table. every record is a tuple in that list. 
    """
    try:
        # Write a query and execute it with cursor
        # Fetch and output resul
        query = 'select * from ' + tablename + ";"
        count = db.cursor.execute(query)
        result = db.cursor.fetchall()
    except sqlite3.Error as error:
        print('Error occured - ', error)
    
    if len(result) == 0:
        print('lege tabel!')
    return result
    
            

def give_record(tablename:str, id:int)->list:
    """returns a a record (line in a table)

    Args:
        tablename (_str_): string containing tablename. For example "tasks"
        id (_int_): ID of the record

    Returns:
        list: list containing a tuple holding the values in the record
    """
    try:
        # Write a query and execute it with cursor
        # Fetch and output resul
        query = 'select * from ' + tablename + ' where id = ' + str(id) +";"
        count = db.cursor.execute(query)
        result = db.cursor.fetchall()
        if len(result) == 0:
            print('lege tabel!')
        return result                            
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



def number_of_records(tablename:str)->int:
    """returns the number of records in a table

    Args:
        tablename (str): name of table

    Returns:
        int: number of records in that table
    """
    try: 
        list_records = give_table(tablename)
        return len(list_records)
    except Exception as e: 
        print(f'problem with number of records: {e}')



def number_of_columns(tablename:str)->int:
    """returns the number of columns in a table

    Args:
        tablename (str): string of the tablename. for example "tasks"

    Returns:
        int: number of columns
    """
    record = give_table(tablename)
    return len(record[0])

    
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


def get_justify_values(tablename:str, table)->list:
    """return the justify values used for "fancyprint"

    Args:
        tablename (_str_): name of table
        

    Returns:
        list: list of the justify values for every column (integer values)
    """
    extra_space = 1
    number_columns = len(table[0])
    number_records = len(table)
    list_justify_values = []
    list_columnames = get_column_names(tablename)
    #f!rst we look for the longest VALUE in a table
    #iterate over the columns
    for column_index in range(number_columns):
        length_longest_string = 0
        #iterate over the records
        for record_index in range(number_records):
            field_value = table[record_index][column_index]
            field_len = len(str(field_value))
            if field_len > length_longest_string: 
                length_longest_string = field_len
        #check if the COLUMNAME  isn't longer then the longest value:         
        len_columname = len(str(list_columnames[column_index]).strip())
        if len_columname > length_longest_string:
            length_longest_string = len_columname
        #append the longest value to the list
        list_justify_values.append(length_longest_string + extra_space)
    return list_justify_values
        

def delete_field():
    pass

