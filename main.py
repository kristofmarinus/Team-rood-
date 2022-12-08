

import database_functions as dbf  #database connection is made in through dbf



def main():
    import databaseconnection as db
    #always rune make_connection first to establish connection with database
    dbf.show_table('tasks') 

    

if __name__ == '__main__':
    main()