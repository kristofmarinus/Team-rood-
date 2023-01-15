import databaseconnection as db  #database connection is made through db
import database_functions as dbf
from task import Task
import inputs
#import users



# actions users:
C_ACTION_MENU_USER = 1
C_ACTION_MENU_TASK = 2
C_ACTION_MAKE_USER = 1
C_ACTION_SHOW_USER = 2
C_ACTION_ADJUST_USER = 3
C_ACTION_DELETE_USER = 4

C_ACTION_MAKE_TASK = 1
C_ACTION_SHOW_TASKS = 2
C_ACTION_CHANGE_PRINT_OPTIONS = 5

C_ACTION_RETURN = 0

C_STOP = 99
C_ACTIONS = [C_ACTION_SHOW_USER,
             C_ACTION_DELETE_USER,
             C_ACTION_RETURN,C_ACTION_ADJUST_USER,]


def menu_header() -> int:

    print("-" * 35)
    print("-" * 35)
    print("MENU")
    print("")
    # user
    print(f"{C_ACTION_MENU_USER}. Users")
    print(f"{C_ACTION_MENU_TASK}. Tasks")
    print(f'{C_STOP}. Stop program')
    print("-" * 35)
    print("-" * 35)

    try:
        print("")
        choice = int(input("Make your choice: "))
    except Exception as e:
        print("Select choice by given number: {}".format(e))
        choice = menu_header()
    return choice


def do_menu():

    loop = True
    while loop:
        choice = menu_header()
        # user mrnu
        if choice == C_ACTION_MENU_USER:
            loop = False
            menu_user()
        if choice == C_ACTION_MENU_TASK:
            loop = False
            do_menu_task()
        if choice == C_STOP:
            loop = False


def menu_header_user():
    print("-" * 35)
    print("-" * 35)
    print("USER MENU")
    print("")
    print(f'{C_ACTION_MAKE_USER}. Create users')
    print(f'{C_ACTION_SHOW_USER}. Show users')
    print(f'{C_ACTION_ADJUST_USER}. ADJUST/UPDATE users')
    print("-" * 35)
    print(f'{C_ACTION_DELETE_USER}. Delete users')
    print("-" * 35)
    print(f'{C_ACTION_RETURN}. Return to main menu')
    print("-" * 35)
    print("-" * 35)


def menu_user():
    """
    this is

    """
    menu_header_user()
    loop = True
    while loop:
        choice = inputs.get_input_item("Choice: ", 1)

        if choice == C_ACTION_MAKE_USER:
            users.add_user()
            menu_header_user()
        if choice == C_ACTION_SHOW_USER:
            users.User.show_users()
            menu_header_user()
        if choice == C_ACTION_DELETE_USER:
            users.delete_user()
            menu_header_user()
        if choice == C_ACTION_ADJUST_USER:
            users.adjust_user_run()
            menu_header_user()
        if choice == C_ACTION_RETURN:
            loop = False
            do_menu()


def menu_header_task()->int: 
    print("-" * 35)
    print("-" * 35)
    print("USER MENU")
    print("")
    print(f'{C_ACTION_MAKE_TASK}. Create task')
    print(f'{C_ACTION_SHOW_TASKS}. Show tasks')
    ##print(f'{C_ACTION_ADJUST_USER}. ADJUST/UPDATE users')
    #print("-" * 35)
    #print(f'{C_ACTION_DELETE_USER}. Delete users')
    #print("-" * 35)
    #print(f'{C_ACTION_RETURN}. Return to main menu')
    print(f'{C_ACTION_CHANGE_PRINT_OPTIONS}. Change display options for tables/records')
    #print("-" * 35)
    #print("-" * 35)
    try:
        print("")
        choice = int(input("Make your choice: "))
    except Exception as e:
        print("Select choice by given number: {}".format(e))
        choice = menu_header()
    return choice

def do_menu_task():
    loop = True
    while loop:
        choice = menu_header_task()
        if choice == C_ACTION_MAKE_TASK:
            pass #aanvulllen!
            loop = False
        if choice == C_ACTION_SHOW_TASKS:
            dbf.print_table("tasks", dbf.give_table_filtered("tasks"))
        if choice == C_ACTION_CHANGE_PRINT_OPTIONS:
            dbf.do_menu_toggle('tasks')


            loop = False



if __name__ == "__main__":
    try:
        db.make_connection()
        do_menu()#
    except Exception as e:
        print(f'something went wrong: {e}')
