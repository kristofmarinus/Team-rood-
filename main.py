

import database_functions as dbf  #database connection is made in through dbf



def main():
    
    #always rune make_connection first to establish connection with database
    #dbf.show_table('tasks')
    #dbf.show_record('tasks', 1)
    #print(dbf.show_field('tasks', 4, 'task_descr'))
    dbf.delete_record('tasks')
    

if __name__ == '__main__':
    main()