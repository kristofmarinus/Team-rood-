import databaseconnection as db  #database  is made in through db
import databaseconnection as db  #database connection is made through db
import database_functions as dbf
import task
import projects
import users
import inputs
import customers


# main actions:
C_ACTION_MENU_USER = 1
C_ACTION_MENU_TASK = 2
C_ACTION_MENU_PROJECT = 3
C_ACTION_MENU_CUSTOMER = 4

# actions users:
C_ACTION_MAKE_USER = 1
C_ACTION_SHOW_USER = 2
C_ACTION_ADJUST_USER = 3
C_ACTION_DELETE_USER = 4

# actions tasks:
C_ACTION_MAKE_TASK = 1
C_ACTION_SHOW_TASKS = 2
C_ACTION_CHANGE_PRINT_OPTIONS = 5

# actions projects:
C_ACTION_MAKE_PROJECT = 1
C_ACTION_SHOW_PROJECTS = 2
C_ACTION_ADJUST_PROJECT = 3
C_ACTION_DELETE_PROJECT = 4

# actions customers:
C_ACTION_MAKE_CUSTOMER = 1
C_ACTION_SHOW_CUSTOMERS = 2
C_ACTION_ADJUST_CUSTOMER = 3
C_ACTION_DELETE_CUSTOMER = 4

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
    print(f"{C_ACTION_MENU_PROJECT}. Projects")
    print(f"{C_ACTION_MENU_CUSTOMER}. Customers")
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
        if choice == C_ACTION_MENU_PROJECT:
            loop = False
            menu_project()
        if choice == C_ACTION_MENU_CUSTOMER:
            loop = False
            menu_customer()
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
    print("TASK MENU")
    print("")
    print(f'{C_ACTION_RETURN}. Return to main menu')
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
            #pass #aanvulllen!
            loop = False
            task.create_task()
            do_menu_task()
        if choice == C_ACTION_SHOW_TASKS:
            dbf.print_table("tasks", dbf.give_table_filtered("tasks"))
        if choice == C_ACTION_RETURN:
            loop = False
            do_menu()
        if choice == C_ACTION_CHANGE_PRINT_OPTIONS:
            dbf.do_menu_toggle('tasks')
            do_menu_task()


            loop = False


def menu_header_projects():
    print("-" * 35)
    print("-" * 35)
    print("PROJECT MENU")
    print("")
    print(f'{C_ACTION_MAKE_PROJECT}. Create project')
    print(f'{C_ACTION_SHOW_PROJECTS}. Show projects')
    print(f'{C_ACTION_ADJUST_PROJECT}. ADJUST/UPDATE project')
    print("-" * 35)
    print(f'{C_ACTION_DELETE_PROJECT}. Delete project')
    print("-" * 35)
    print(f'{C_ACTION_RETURN}. Return to main menu')
    print("-" * 35)
    print("-" * 35)


def menu_project():
    """
    this is

    """
    menu_header_projects()
    loop = True
    while loop:
        choice = inputs.get_input_item("Choice: ", 2)

        if choice == C_ACTION_MAKE_PROJECT:
            projects.add_project()
            menu_header_projects()
        if choice == C_ACTION_SHOW_PROJECTS:
            projects.Project.show_projects()
            menu_header_projects()
        if choice == C_ACTION_DELETE_PROJECT:
            projects.delete_project()
            menu_header_projects()
        if choice == C_ACTION_ADJUST_PROJECT:
            projects.adjust_project_run()
            menu_header_projects()
        if choice == C_ACTION_RETURN:
            loop = False
            do_menu()

def menu_header_customers():
    print("-" * 35)
    print("-" * 35)
    print("CUSTOMER MENU")
    print("")
    print(f'{C_ACTION_MAKE_CUSTOMER}. Create customer')
    print(f'{C_ACTION_SHOW_CUSTOMERS}. Show customers')
    print(f'{C_ACTION_ADJUST_CUSTOMER}. ADJUST/UPDATE customer')
    print("-" * 35)
    print(f'{C_ACTION_DELETE_CUSTOMER}. Delete customer')
    print("-" * 35)
    print(f'{C_ACTION_RETURN}. Return to main menu')
    print("-" * 35)
    print("-" * 35)


def menu_customer():
    """
    this is

    """
    menu_header_customers()
    loop = True
    while loop:
        choice = inputs.get_input_item("Choice: ", 2)

        if choice == C_ACTION_MAKE_CUSTOMER:
            customers.add_customer()
            menu_header_customers()
        if choice == C_ACTION_SHOW_CUSTOMERS:
            customers.Customer.show_customers()
            menu_header_customers()
        if choice == C_ACTION_DELETE_CUSTOMER:
            customers.delete_customer()
            menu_header_customers()
        if choice == C_ACTION_ADJUST_CUSTOMER:
            customers.adjust_customer_run()
            menu_header_customers()
        if choice == C_ACTION_RETURN:
            loop = False
            do_menu()



if __name__ == "__main__":
    try:
        db.make_connection()
        do_menu()
    except Exception as e:
        print(f'something went wrong: {e}')
