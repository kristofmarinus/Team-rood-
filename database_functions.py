

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


def print_record(tablename:str, result:list, list_justify = [], no_columnames = False):
    """prints a single record (given as parameter: "result")
    when called by the function "print_table" the list_justify has to be given by the print_table function 
    and no_columnnames set to True.
    print_record does not GET the record. use "give_record" for that and feed it as parameter "result"

    Args:
        tablename (str): string containing the tablename. for example "tasks"
        result (): the result of the query. A list containing a single tuple holding the values in the record
        list_justify (list, optional): list of justication values. Defaults to []. only enter this when printing multiple records (like a table)
        no_columnames (bool, optional): set this to True when printing multiple records (like a table). Defaults to False.
    """
    if len(list_justify) == 0:
        list_justify = get_justify_values(tablename, result)
    number_colums = number_of_columns(tablename)

    if no_columnames == False: 
        #get and print the columnames:
        string_record = give_string_columnames(tablename, list_justify)
        print(string_record)
    #iterete over the list "result" and compile the string that gets printed: 
    string_record = ''
    for index in range(number_colums):
        string_record += '| ' + str(result[0][index]).strip().ljust(list_justify[index]) 
    #print the string: 
    print(string_record + '| ')


def print_table(tablename:str, result:list):
    """prints a table. Or part of a table (for example the result of a query)
    print_table does not GET the table from the database. Use in combination with get_table() and feed that value into the function as "result"

    Args:
        tablename (str): string containing the tablename. for example "tasks"
        result (list): hold the table (or result of a query0). A list containing tuples. Every tuple holds the values of a record (line) 
    """
    if len(result) == 0:
        print('lege tabel!')
    list_justify = get_justify_values(tablename, result)
    number_colums = number_of_columns(tablename)
   #print columnames:   
    print(give_string_columnames(tablename, list_justify))    
    #iterate over the table and print every record:  
    number_records = len(result)
    for record_index in range(number_records):  
        print_record(tablename, [result[record_index]], list_justify, True) 

      
  
def give_string_columnames(tablename:str, list_justify:list)->str:
    """returns a string of columnames, used in print_table() and print_record()

    Args:
        tablename (_str_): name of the table
        list_justify(_list_): list containing the justify values for printing

    Returns:
        _str_: formatted string of the columnames
    """
    try: 
        query = 'select * from ' + tablename + ";"
        count = db.cursor.execute(query)
        result = db.cursor.fetchall()
        #list_justify = get_justify_values(tablename)
        number_colums = number_of_columns(tablename)
        list_column_names = get_column_names(tablename)
        string_columnames = ''
        for index in range(number_colums):
            string_columnames += '| ' + str(list_column_names[index]).strip().ljust(list_justify[index]) 
        return string_columnames + '| '
    except sqlite3.Error as error:
        print('Error occured - ', error)



def give_field(tablename:str, id:int, fieldname:str):
    """returns value of a field

    Args:
        tablename (str): name of table
        id (int): id of record
        fieldname (str): colunmname

    Returns:
        _type_: value in that field. type depends on value...
    """
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
        

def give_index_values(table:list)->list:
    pass #returns a list with the index values


def get_column_names(tablename:str)->list:
    """generates a list of the column names of a given table

    Args:
        tablename (_type_): name of the table

    Returns:
        list: list containing the names of the columns (string)
    """
    table = db.cursor.execute(f'select * from {tablename}')
    description = table.description
    list_names = []
    for element in description:
        list_names.append(str(element[0]))
    return list_names

    





