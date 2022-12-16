

#sqllite3 imported through databaseconnection
import databaseconnection as db
import sqlite3

def give_table(tablename, fancy_print = False):
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
    if not fancy_print: 
        return result
    elif fancy_print:
        print_string = give_string_columnames(tablename) + "\n"        
        number_records = number_of_records(tablename)
        for record_index in range(1,number_records):  #dit moet worden aangepast nog.. range moet een lijst van indexen worden (want index kan ontbreken)
            print_string += give_record(tablename, record_index, True, True) + "\n"
        return print_string
            

def give_record(tablename, id, Fancyprint = False, multiple_records = False):

    try:
        # Write a query and execute it with cursor
        # Fetch and output resul
        query = 'select * from ' + tablename + ' where id = ' + str(id) +";"
        count = db.cursor.execute(query)
        result = db.cursor.fetchall()
    
        if len(result) == 0:
            print('lege tabel!')
        else:
            if not Fancyprint: 
                return result
            elif Fancyprint:
                list_justify = get_justify_values(tablename)

                number_colums = number_of_columns(tablename)
                string_columnames = give_string_columnames(tablename)
                string_record = ''
                for index in range(number_colums):
                    string_record += '| ' + str(result[0][index]).strip().ljust(list_justify[index]) 
                if multiple_records == False: 
                    return string_columnames + "\n" + string_record + '| '
                if multiple_records == True: 
                    return string_record + '| '      
    except sqlite3.Error as error:
        print('Error occured - ', error)


def give_string_columnames(tablename:str)->str:
    """returns a string of columnames, used in fancyprint

    Args:
        tablename (_str_): name of the table

    Returns:
        _str_: formatted string of the columnames
    """
    try: 
        query = 'select * from ' + tablename + ";"
        count = db.cursor.execute(query)
        result = db.cursor.fetchall()
        list_justify = get_justify_values(tablename)
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


def get_justify_values(tablename:str)->list:
    """return the justify values used for "fancyprint"

    Args:
        tablename (_str_): name of table

    Returns:
        list: list of the justify values for every column (integer values)
    """
    extra_space = 1
    table = give_table(tablename)
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
        

def give_index_values(tablename:str)->list:
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

    





