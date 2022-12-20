

import database_functions as dbf  #database connection is made in through dbf
from task import Task
import datetime


def main():

    #always rune make_connection first to establish connection with database
    #print(type(dbf.number_of_columns('tasks')))
    #print(dbf.get_justify_values('tasks'))
    #print(dbf.give_record('tasks', 1, True))
    #dbf.print_record('tasks', dbf.give_record('tasks', 1))
    #dbf.print_record('tasks', dbf.give_record('tasks', 2))
    #dbf.print_record('tasks', dbf.give_record('tasks', 3))
    #print(dbf.show_field('tasks', 4, 'task_descr'))
    #dbf.print_table('customers', dbf.give_table('customers'))
    #print(len(dbf.give_table('tasks')))
    #print(len(dbf.give_table('tasks')[0]))
    #print(dbf.get_justify_values(dbf.give_table('tasks'), 'tasks'))
    #print(dbf.give_column_names('tasks'))
    #print(dbf.give_field('tasks', 1, 'task_descr'))
    new_task = Task()
    new_task.task_descr = 'test 6 toevoegen'
    new_task.fk_user_id = 2
    new_task.fk_project_id = 1
    new_task.task_deadline = datetime.date(1987,5,6)
    print(new_task.task_deadline)
    print(type(new_task.task_deadline))
    new_task.to_db()
    
    #print(type(new_task))
    #new_task.from_sql = 2
    #print(new_task.__dict__)



if __name__ == '__main__':
    main()