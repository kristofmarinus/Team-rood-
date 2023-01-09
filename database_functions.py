

#sqllite3 imported through databaseconnection
import databaseconnection as db
import sqlite3
from os import path

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


def print_record(tablename:str, result:list, list_justify = [], no_columnames = False, filtered = True):
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
    number_colums = len(result[0])

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
    number_colums = len(result[0])
   #print columnames:   
    print(give_string_columnames(tablename, list_justify))    
    #iterate over the table and print every record:  
    number_records = len(result)
    for record_index in range(number_records):  
        print_record(tablename, [result[record_index]], list_justify, True) 

      
  
def give_string_columnames(tablename:str, list_justify:list, filtered = True)->str:
    """returns a string of columnames, used in print_table() and print_record()

    Args:
        tablename (_str_): name of the table
        list_justify(_list_): list containing the justify values for printing
        filtered(bool): set to False to get ALL columnnames in that table

    Returns:
        _str_: formatted string of the columnames
    """
    try: 
        if filtered == False: 
            query = 'select * from ' + tablename + ";"
            count = db.cursor.execute(query)
            result = db.cursor.fetchall()
            number_colums = len(list_justify)
            list_column_names = get_column_names(tablename)
        elif filtered == True: 
            list_column_names = get_columns_shown(tablename)
        number_colums = len(list_justify)
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


def get_justify_values(tablename:str, table:list, filtered = True)->list:
    """return the justify values used for print table. 

    Args:
        tablename (_str_): name of table
        table (_list_): 
        filtered (_bool_): set to False if you want justify list for ALL the columnnames
        

    Returns:
        list: list of the justify values for every column in the table or filtered table (integer values)
    """
    extra_space = 1
    number_columns = len(table[0])
    number_records = len(table)
    list_justify_values = []
    if filtered:
        list_columnames = get_column_names_filtered(tablename)
    if not filtered: 
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

def newline_removed(list_input:list)->list:
    """removes the "new line" character "\n" from every element in a list

    Args:
        list_input (list): list of strings

    Returns:
        list: list with "\n" removed 
    """
    list_output = []
    for line in list_input:
            list_output.append(line.replace('\n',''))
    return list_output


def newline_added(list_input: list)->list:
    """adds the "new line" character "\n" to every element in a list

    Args:
        list_input (list): list of strings

    Returns:
        list: list with "\n" added 
    """

    list_output = []
    for line in list_input:
        line_with_newline = line + "\n"
        list_output.append(line_with_newline)
    return list_output


def make_filename(tablename:str)->str:
    """returns filename for the .txt file where the settings for showing columns in a table are stored

    Args:
        tablename (str): string of tablename. for example "tasks"

    Returns:
        _str_: string of filename. for exameple: "column_names_shown_tasks.txt"
    """
    #make a string holding the filename:
    filename = "column_names_shown_" + tablename + ".txt"
    return filename


def get_columns_shown(tablename:str)->list:
    """reads the columnnames from .txt files and returns a list containing the columnnames

    Args:
        tablename (str): string of the tablename. for example "tasks"

    Returns:
        list: list containing the columnnames in the .txt file
    """
    filename = make_filename(tablename)
    #check that the file exists. if so: read the file. if not: give a message and return an empty list
    if not path.exists(filename):
        print(f'filename: {filename}  is not found! ')
        return []
    #read the file and write the contents into a list "list columnnames":    
    try: 
        with open(filename, 'r') as f:
            list_with_newline = f.readlines()
            list_columnames_shown = newline_removed(list_with_newline)
    except Exception as e:
        print(f'could not read from file {filename}: {e}')  
        return []
    #check that the columnnames are still in the table and remove the ones that are not
    list_columnnames = get_column_names(tablename)
    for columnname in list_columnames_shown:
        if columnname not in list_columnnames:
            print(f'columnname:"{columnname}" is in file "{filename}" but no longer in table {tablename}! it will be removed from {filename} ')
            list_columnames_shown.remove(columnname)
    #check for double values and if so: remove:
    for columnname in list_columnames_shown:
        if list_columnames_shown.count(columnname) > 1:
            print(f'value {columnname} appears multiple times')
            list_columnames_shown.remove(columnname)
    return list_columnames_shown


def save_columns_shown(tablename:str, list_columnnames_shown:list):
    """saves (or overwrites) in a .txt file the columnnames in a list

    Args:
        tablename (str): string of tablename. for example: "tasks"
        list_columnnames_shown (list): list of the columnnames that will be displayed
    """
    filename = make_filename(tablename)
    try:
        with open(filename, 'w') as f:
            list_columnames = newline_added(list_columnnames_shown)
            for columnname in list_columnames:
                f.write(columnname)
    except Exception as e:
        print(f'error saving columns shown: {e}')

    

def get_columns_not_shown(list_all_columnnames:list, list_columns_shown:list)->list: 
    """returns list of colummnames not displayed

    Args:
        list_all_columnnames (list): list of all the columnnames. use function get_column_names()
        list_columns_shown (list): list of the columns that are displayed

    Returns:
        list: list of the columns that are not displayed
    """
    list_columns_not_shown = []
    for columnname in list_all_columnnames:
        if columnname not in list_columns_shown:
            list_columns_not_shown.append(columnname)
    return list_columns_not_shown
    

def show_options_toggle(tablename, list_columns_shown:list, list_columns_not_shown: list):
    """handles the menu for changing the columns that are/are not displayed in table view. called by do_menu_toggle

    Args:
        tablename (_type_): string of tablename. for example: "tasks"
        list_columns_shown (list): list containing the columns that are displayed
        list_columns_not_shown (list): list containing the columns that are not displayed

    """
    #make list with indexes "A" for columnnames that are shown:
    list_index_a = []
    for index in range(len(list_columns_shown)):
        text = "A" + str(index+1)
        list_index_a.append(text)
    #make list with indexes "B"
    list_index_b = []
    for index in range(len(list_columns_not_shown)):
        text = "B" + str(index+1)
        list_index_b.append(text)
    #assign some values to paramaters for later use in for-loops
    length_list_columns_shown = len(list_columns_shown)
    length_list_columns_not_shown = len(list_columns_not_shown)
    string_columnnames_shown= "COLUMNNS SHOWN"
    string_columnnames_not_shown= "COLUMNNS NOT SHOWN"
    length_longest_list = max(length_list_columns_shown, length_list_columns_not_shown)
    len_longest_columnname = max(20, len(string_columnnames_shown))
    if len(list_columns_shown) > 0:
        len_longest_columnname = max(len(max(list_columns_shown, key=len)), len(string_columnnames_shown))
    else: 
        len_longest_columnname = max(20, len(string_columnnames_shown))
    #print menu header:
    print("\n"+ string_columnnames_shown.ljust(7 + len_longest_columnname)+ " | "  + string_columnnames_not_shown + "\n")
    #print menu "body"
    for i in range(length_longest_list):
        string_print = ""
        if i < length_list_columns_shown:
            string_print += list_index_a[i].ljust(4) + list_columns_shown[i].ljust(len_longest_columnname + 3) + " | " 
        else: 
            string_print += " " * (7 + len_longest_columnname)  + " | " 
        if i < length_list_columns_not_shown:
            string_print += list_index_b[i].ljust(4) + list_columns_not_shown[i]
        print(string_print)
    print("\n")
    #get user input:
    user_choice = input('give the index of the columnname you want to toggle, or type SAVE or type STOP: ')
    #action based on user input: 
    if user_choice.lower().strip() == "stop":
        pass  # this has to become: return to main menu....
    elif user_choice.lower().strip() == "save":
        save_columns_shown(tablename, list_columns_shown)

    elif user_choice.upper() in list_index_a:
        index = int(user_choice[1:])-1
        columnname = list_columns_shown[index]
        list_columns_not_shown.append(columnname)
        list_columns_shown.pop(index)
        return show_options_toggle(tablename, list_columns_shown, list_columns_not_shown)
    elif user_choice.upper() in list_index_b:
        index = int(user_choice[1:])-1
        columnname = list_columns_not_shown[index]
        list_columns_shown.append(columnname)
        list_columns_not_shown.pop(index)
        return show_options_toggle(tablename, list_columns_shown, list_columns_not_shown)
    else: 
        print('invalid choice! try again! ')
        return show_options_toggle(tablename, list_columns_shown, list_columns_not_shown)
 

def get_column_names_filtered(tablename:str)->list:
    """returns a list with the column names that will be shown. The main purpose of this function is SORTING the list of column names 

    Args:
        tablename (string): string of tablenames, for example "tasks"

    Returns:
        list: sorted list of the column names that will be displayed
    """
    all_column_names = get_column_names(tablename)
    column_names_shown = get_columns_shown(tablename)
    column_names_filtered = []
    for column_name in all_column_names:
        if column_name in column_names_shown:
            column_names_filtered.append(column_name)
    return column_names_filtered



def filter_list(tablename:str)->list:
    """generated a list of True or False values. for every columnname in the table that value showes if it is displayed or not

    Args:
        tablename (str): string of tablename. for example: "tasks"

    Returns:
        list: list with same length as number of columns of the table; Every value is True: column is displayed, or False: column is not displayed
    """
    all_column_names = get_column_names(tablename)
    column_names_shown = get_columns_shown(tablename)
    filter = []
    for column_name in all_column_names:
        if column_name in column_names_shown:
            filter.append(True)
        else:
            filter.append(False)
    return filter


def give_record_filtered(tablename:str, id:int)->list:
    """return the filtered version of the record (only with the columns that are to be displayed)

    Args:
        tablename (str): string of the tablename, for example "tasks"
        id (int): id of the record

    Returns:
        list: record with only the displayed columns
    """
    tupple_record = give_record(tablename,id)[0]
    list_record = list(tupple_record)
    filter = filter_list(tablename)
    list_record_filtered = []
    for index in range(len(list_record)):
        if filter[index]:
            list_record_filtered.append(list_record[index])
    # return a list containing list_record_filtered (because function give_record gives similar return)
    return [list_record_filtered]



def give_table_filtered(tablename:str)->list:
    """returns the filtered version of the table (only with the columns that are to be displayed)

    Args:
        tablename (str): string of tablename, for example: "tasks"

    Returns:
        list: list containing lists (every sublist is a record)
    """
    table_unfiltered = give_table(tablename)
    filter = filter_list(tablename)
    table_filtered = []
    for record in table_unfiltered:
        list_record = list(record)
        record_filtered = []
        for index in range(len(list_record)):
            if filter[index]:
                record_filtered.append(list_record[index])
        table_filtered.append(record_filtered)
    return table_filtered
    





def do_menu_toggle(tablename:str):
    """handles the menu for changing the columns that are/are not displayed in table view.

    Args:
        tablename (str): string of tablename. for example: "tasks"
    """
    
    #initialize list_columnnames shown and list_columnnames_not_shown
    list_columnnames_shown = get_columns_shown(tablename)
    list_all_columnnames = get_column_names(tablename)
    list_columnnames_not_shown = get_columns_not_shown(list_all_columnnames, list_columnnames_shown)
    #call function that handles the rest: 
    show_options_toggle(tablename, list_columnnames_shown, list_columnnames_not_shown)




    


    
def main():
    #do_menu_toggle("customers")
    #print(get_column_names_filtered("tasks"))
    #print(give_record("tasks", 1))
    #print(give_record_filtered("tasks", 1))
    #print(get_justify_values("tasks" ,give_record_filtered("tasks", 1)))
    print_record("users",give_record_filtered("users", 1), get_justify_values("tasks" ,give_record_filtered("tasks", 1)))
    print_table("tasks", give_table_filtered('tasks'))


if __name__ == '__main__':
    main()




