

import database_functions as dbf  #database connection is made in through dbf
from task import Task


def main():

    #always rune make_connection first to establish connection with database
    #print(type(dbf.number_of_columns('tasks')))
    #print(dbf.get_justify_values('tasks'))
    #print(dbf.give_record('tasks', 1, True))
    #dbf.show_record('tasks', 1)
    #print(dbf.show_field('tasks', 4, 'task_descr'))
    print(dbf.give_table('tasks', True))
    #print(len(dbf.give_table('tasks')))
    #print(len(dbf.give_table('tasks')[0]))
    #print(dbf.get_justify_values(dbf.give_table('tasks'), 'tasks'))
    #print(dbf.give_column_names('tasks'))
    

if __name__ == '__main__':
    main()