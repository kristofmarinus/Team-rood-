import databaseconnection as db
import database_functions as dbf
from inputs import get_input_item,get_int
import sqlite3
from get_input import get_input

class User():
    __id = ""
    __firstname = ""
    __lastname = ""
    __fullname = ""
    __email = "none"
    __website = "none"



    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        self.__firstname = value

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value: str):
        if "." in value and "@" in value:
            self.__email = value
        else:
            print("invalid email address")
            self.__email = "n/a"

    @property
    def website(self):
        return self.__website

    @website.setter
    def website(self, value: str):
        if '.' in value:
            self.__website = value
        else:
            print('invalid website')
            self.__website = 'n/a'

    @property
    def fullname(self) -> str:
        """generates the full name of the user, based on the first and last name

        Returns:
            str: the full name of the user
        """
        return self.__firstname + " " + self.__lastname

    def write_user(self):
        """writes user to the database
        """
        try:
            sql_cmd = f"insert into users (fullname,first_name, last_name, email, website) values ('{self.fullname}','{self.firstname}', '{self.lastname}', '{self.email}', '{self.website}');"
            db.cursor.execute(sql_cmd)
            db.sqliteConnection.commit()
        except Exception as e:
            print(f'fout def.write_user: {e}')

    @staticmethod
    def delete_user(inp: int):
        """delete user from database

        Args:
            inp (int): id nr of user to be deleted
        """
        try:
            sql_cmd = f'delete from users where id = {inp};'
            db.cursor.execute(sql_cmd)
            db.sqliteConnection.commit()
            print('User deleted')
        except Exception as e:
            print(f'fout: {e}')

    @staticmethod
    def show_users(project_id=-1):
        """show all users
        """
        project_id = get_input_item("Enter 1 to show all users",
                                    1)
        #Add a feature to show users from X-ids to Y-ids.
        def show_users_2(project_id):
            try:
                if project_id == 1:
                    sql_cmd = 'select * from users;'
                db.cursor.execute(sql_cmd)
                rows = db.cursor.fetchall()
                print('-' * 50)
                print('user ID - fullname - firstname - lastname - email - website')
                print('-' * 50)
                if len(rows) > 0:
                    for row in rows:
                        print('| ', end='')
                        for i in row:
                            print(i, end=' | ')
                        print('')
                else:
                    print('geen gegevens gevonden')
            except Exception as e:
                print(f'fout: {e}')
        show_users_2(project_id)


        
    def print_tasks(self):
        try:
            # Write a query and execute it with cursor
            # Fetch and output resul
            query = f'select * from tasks where fk_user_id = "{self.id}";'
            #query = 'select * from users ;'
            count = db.cursor.execute(query)
            result = db.cursor.fetchall()
            if len(result) != 0: 
                filtered_result = dbf.filter_result('tasks', result)
                dbf.print_table('tasks', filtered_result)
            else:
                print("user has no tasks assigned! ")
        except sqlite3.Error as error:
            print('Error occured - ', error)
        


def create_user() -> User:
    """

    Asks for information

    Returns:
        User: the user
    """
    firstname = get_input_item('Give first name')
    lastname = get_input_item('Give last name')
    email = get_input_item('Give email')
    website = get_input_item('Give website')
    user = User()
    user.firstname = firstname
    user.lastname = lastname
    user.email = email
    user.website = website
    return user


def add_user():
    """
    adds a user to the user list
    """
    user = create_user()
    user.write_user()


def delete_user():
    """asks user which id to delete,

    double check : yes/no

    deletes the user
    """
    User.show_users()
    inp = get_input_item("Select user id to delete", 1)
    check = get_input_item(f'WARNING: Delete is irreparable --- enter "y" --- if you wish still to delete the user{inp}')
    if check.strip().lower() == "y":
        User.delete_user(inp)
        print(f'USER with id:{inp} was DELETED')
    else:
        print('Deletion was UNDONE.')
    # UPDATE ALL TASKS WHICH DELETED ID = USER ID


def adjust_user(db):

        def print_all():
            """
            #Print all the info of the table users
            :return: prints all the users
            """
            sql_cmd = 'select * from users;'
            db.cursor.execute(sql_cmd)
            rows = db.cursor.fetchall()
            print('-' * 50)
            print('user ID - fullname - firstname - lastname - email - website')
            print('-' * 50)
            if len(rows) > 0:
                for row in rows:
                    print('| ', end='')
                    for i in row:
                        print(i, end=' | ')
                    print('')
                print('-' * 50)
            else:
                print('geen gegevens gevonden')
        print_all()

        # Choose id of the user
        user_id = get_int("Enter the id of the user: ")

        #cheking if the id of the user exists
        def id_exists(user_id):
            db.cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
            result = db.cursor.fetchone()
            if result:
                return True
            else:
                return False

        # IF given id NOT exists restart the main function -> adjust_user()


        #if it is ok then print the user details
        if id_exists(user_id):
            return user_id

        if id_exists(user_id) is False:
            print("ID does not exist in the table")
            print("Choose another one")
            adjust_user(db)
        return user_id

#function to print_selected_user
def print_selected_user(user_id):
    # print the selected USER
    db.cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    rows = db.cursor.fetchall()
    print('-' * 50)
    print('user ID - fullname - firstname - lastname - email - website')
    print('-' * 50)
    for row in rows:
        print('| ', end='')
        for i in row:
            print(i, end=' | ')
        print('')
    print('-' * 50)


def adjust_row(user_id):
    # Ask for all the details
    fname = get_string("Enter the first name: ")
    lname = get_string("Enter the last name: ")
    email = input("Enter the email: ")
    website = input("Enter the website: ")

    # Update the row in the database
    c = db.cursor
    c.execute("UPDATE users SET firstname=?, lastname=?, email=?, website=? WHERE id=?",
              (fname, lname, email, website, user_id))
    db.sqliteConnection.commit()
    #autoupdate the full name
    c.execute("UPDATE users SET fullname=firstname || ' ' || lastname WHERE id=?", (user_id,))
    db.sqliteConnection.commit()
    print("User details updated successfully!")


def adjust_column(user_id):
    # Query the database to get a list of column names in the USERS table
    c = db.cursor
    c.execute("PRAGMA table_info(users)")
    column_names = [column_info[1] for column_info in c.fetchall()]

    # Ask for the column to be adjusted
    column = input("Enter the column name to be adjusted: ")
    while column not in column_names or column == 'fullname':
        if column == 'fullname':
            print("You cannot adjust fullname, to adjust it u need to change firstname or lastname")
            column = input("Enter the column name to be adjusted: ")
        else:
            print("Invalid column name. Please try again.")
            column = input("Enter the column name to be adjusted: ")

    # Update the column in the database
    value = input("Enter the new value: ")
    c.execute("UPDATE users SET {}=? WHERE id=?".format(column), (value, user_id))
    db.sqliteConnection.commit()
    # autoupdate the full name
    c.execute("UPDATE users SET fullname=first_name || ' ' || last_name WHERE id=?", (user_id,))
    db.sqliteConnection.commit()
    print("User details updated successfully!")


def adjust_type_func(user_id):
    """
            # Do you want to adjust whole row or specific column
    :return: row or column
    """
    adjust_type = get_int("Choose what do you want to adjust:"
                               "\n1.whole row "
                               "\n2.specific column "
                               "\nChoose: ")
    if adjust_type == 1:
        print_selected_user(user_id)
        adjust_row(user_id)
        return adjust_type

    elif adjust_type ==2:
        print('2')
        print_selected_user(user_id)
        adjust_column(user_id)
        return adjust_type

    else:
        print('Choose a valid number!')
        adjust_type_func(user_id)


def more_adjustments():
    """
    asks the person if he wants to adjust row/column of the same user
    or choose another user
    or go back / exit
    :return:
    """
    more = get_int(
        ("Do you want to "
         "\n1. adjust row/column of the same user  "
         "\n2. choose another user  "
         "\n3. exit"
         "\nChoose: "))
    return more


def extra(user_id,more):
    while True:
        # Ask if user wants to adjust more column or choose another row/user
        if more == 1:  # adjust same user
            adjust_type_func(user_id)
            more_adjustments()
        elif more == 2:  # another row/user
            adjust_user(db)
            adjust_type_func(user_id)
            more_adjustments()
        elif more == 3:
            break


def adjust_user_run():
    # Connect to the database
        # Adjust user details
        user_id = adjust_user(db)
        adjust_type_func(user_id)
        more = more_adjustments()
        extra(user_id,more)


def select_user()->User:
    #print table with all the users: 
    print("SELECT A USER:")
    print("These are all the users: ")
    dbf.print_table("users", dbf.give_table_filtered("users"))
    #get user input: 
    while True: 
        user_choice = get_input('give the ID of the user you choose: ', 1)
        #test if user input is in the list of tasks: 
        list_task_id = dbf.give_id_table('users')
        if user_choice in list_task_id:
            chosen_user = User()
            #get property values from database (there is no function yet for this..)
            #we are only setting the id for now... 
            chosen_user.id = user_choice
            return chosen_user
        else: 
            print("invalid id... please choose an id from the list! ")



def all_tasks_user():
    """handles printing all the tasks for a user that is selected through input
    """
    #first select a user: 
    user_selected = select_user()
    #print all tasks for this user: 
    print("-" * 35)
    print("-" * 35)
    print("All tasks for the user you selected: ")
    print("")
    user_selected.print_tasks()




def main():
    #user_test = select_user()
    pass
    #user_test.print_tasks()


if __name__ == '__main__':
    main()


#1 error cant fix: after making mistake of choosing the users to adjust,
# we choose specific column and PRINTING does not show the information about user.


#make maybe custom get_email function? in library
#make maybe custom get_website function? in library




#test1 - Users - Adjust - ID of the user:
    #put letter - FIXED
    #put unknown id - fixed

#test2 - Users - Adjust - ID of the user - specific column
    #put a mistake in a name of the column - FIXED!!
    #if the column != column in USERS then ask again for the column! -- FIXED!!

#test3 - Users - Adjust - ID of the user - whole row
    # error on whole row adjustment - syntax error WHERE etc -FIXED!!!!

#test4 - Users - Adjust - ID of the user - specific column - Adjust row/column of the same user
 #-fixed


#problem the full name does not updates after the chaning the firstname or lastname --- FIXED!!!

