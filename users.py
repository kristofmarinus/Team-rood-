import databaseconnection as db
from inputs import get_input_item


class User():
    __firstname = ""
    __lastname = ""
    __fullname = ""
    __email = "none"
    __website = "none"

    def __init__(self, firstname: str, lastname: str):
        self.__firstname = firstname
        self.__lastname = lastname

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
    user = User(firstname, lastname)
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
    # UPDATE ALL TAASKS WHICH DELETED ID = USER ID


def adjust_user(db):
        #Print all the info of the table users
        sql_cmd = 'select * from users;'
        dbf.cursor.execute(sql_cmd)
        rows = dbf.cursor.fetchall()
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

        # Choose id of the user
        print('-' * 50)

        user_id = int(input("Enter the id of the user: "))

        # Do you want to adjust whole row or specific column
        adjust_type = int(input("\n1.whole row \n2.specific column \nWhat do you want to adjust: "))

        if adjust_type == 1:
            # Ask for all the details
            fname = input("Enter the first name: ")
            lname = input("Enter the last name: ")
            email = input("Enter the email: ")
            website = input("Enter the website: ")

            # Update the row in the database
            c = db.cursor
            c.execute("UPDATE users SET firstname=?, lastname=?, email=?, website=?, WHERE id=?",
                      (fname, lname, email,website, user_id))
            db.sqliteConnection.commit()
            print("User details updated successfully!")
        elif adjust_type == 2:
            # Ask for the column to be adjusted
            column = input("Enter the column name to be adjusted: ")
            value = input("Enter the new value: ")

            # Update the column in the database
            c = db.cursor
            c.execute("UPDATE users SET {}=? WHERE id=?".format(column), (value, user_id))
            db.sqliteConnection.commit()
            print("User details updated successfully!")


def adjust_user_run():
    # Connect to the database

    while True:
        # Adjust user details
        adjust_user(db)

        # Ask if user wants to adjust more column or choose another row/user
        more = int(
            input("Do you want to "
                  "\n1. adjust more column of the user  "
                  "\n2. choose another row/user  "
                  "\n3. exit"
                  "\nChoose: "))
        if more == 1:
            #Choose the column
            continue
        elif more == 2:
            #Choose another user
            continue
        elif more == 3:
            #exit
            break


