import databaseconnection as db
from inputs import get_input_item
from src import cs50
import database_functions as dbf
import sqlite3
from projects import Project
from task import Task


class Customer():
    __customer_name = ""
    __customer_website = "none"
    __customer_phone = ""
    __vat_number = "none"

    def __init__(self, customer_name: str, customer_phone : str):
        self.__customer_name = customer_name
        self.__customer_phone = customer_phone

    @property
    def customer_name(self):
        return self.__customer_name

    @customer_name.setter
    def customer_name(self, value):
        if value is not None:
            self.__customer_name = value

    @property
    def customer_website(self):
        return self.__customer_website

    @customer_website.setter
    def customer_website(self, value):
        if value is not None:
            self.__customer_website = value

    @property
    def customer_phone(self):
        return self.__customer_phone

    @customer_phone.setter
    def customer_phone(self, value):
        if value is not None:
            self.__customer_phone = value

    @property
    def vat_number(self):
        return self.__vat_number

    @vat_number.setter
    def vat_number(self, value):
        if value is not None:
            self.__vat_number = value


    def write_customer(self):
        """writes customer to the database
        """
        try:
            sql_cmd = f"insert into customers (customer_name, customer_website, customer_phone, vat_number) values ('{self.customer_name}','{self.customer_website}', '{self.customer_phone}', '{self.vat_number}');"
            db.cursor.execute(sql_cmd)
            db.sqliteConnection.commit()
        except Exception as e:
            print(f'fout def.write_customer: {e}')

    @staticmethod
    def delete_customer(inp: int):
        """delete customer from database

        Args:
            inp (int): id nr of customers to be deleted
        """
        try:
            sql_cmd = f'delete from customers where id = {inp};'

            
            db.cursor.execute(sql_cmd)
            db.sqliteConnection.commit()
            print('customer deleted')
        except Exception as e:
            print(f'fout: {e}')

    @staticmethod
    def show_customers(project_id=-1):
        """show all customers
        """
        project_id = get_input_item("Enter 1 to show all customers",
                                    1)
        #Add a feature to show customers from X-ids to Y-ids.
        def show_customers_2(project_id):
            try:
                if project_id == 1:
                    sql_cmd = 'select * from customers;'
                db.cursor.execute(sql_cmd)
                rows = db.cursor.fetchall()
                print('-' * 50)
                print('customer ID - customer_name - customer_website - customer_phone - vat_number')
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
        show_customers_2(project_id)


def create_customer() -> Customer:
    """

    Asks for information

    Returns:
        Customer: the customer
    """
    customer_name = get_input_item('Give customer name')
    customer_website = get_input_item('Give customer website')
    customer_phone = get_input_item('Give customer phone number')
    vat_number = get_input_item('Give vat number')
    customer = Customer(customer_name, customer_phone)
    customer.website = customer_website
    customer.vat_number = vat_number
    return customer


def add_customer():
    """
    adds a customer to the customer list
    """
    customer = create_customer()
    customer.write_customer()


def delete_customer():
    """asks user which id to delete,

    double check : yes/no

    deletes the customer
    """
    Customer.show_customers()
    inp = get_input_item("Select customer id to delete", 1)
    check = get_input_item(f'WARNING: Delete is irreparable --- enter "y" --- if you wish still to delete the customer{inp}')
    if check.strip().lower() == "y":
        Project.delete_projects_by_customer_id(inp)
        Task.delete_tasks_by_project_id(inp)
        Customer.delete_customer(inp)
        print(f'CUSTOMER with id:{inp} was DELETED')
    else:
        print('Deletion was UNDONE.')


def adjust_customer(db):

        def print_all():
            """
            Print all the info of the table customers
            :return: prints all the customers
            """
            sql_cmd = 'select * from customers;'
            db.cursor.execute(sql_cmd)
            rows = db.cursor.fetchall()
            print('-' * 50)
            print('customer ID - customer_name - customer_website - customer_phone - vat_number')
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

        # Choose id of the customer
        customer_id = cs50.get_int("Enter the id of the customer: ")

        #cheking if the id of the customer exists
        def id_exists(customer_id):
            db.cursor.execute("SELECT * FROM customers WHERE id=?", (customer_id,))
            result = db.cursor.fetchone()
            if result:
                return True
            else:
                return False

        # IF given id NOT exists restart the main function -> adjust_customer()


        #if it is ok then print the customer details
        if id_exists(customer_id):
            return customer_id

        if id_exists(customer_id) is False:
            print("ID does not exist in the table")
            print("Choose another one")
            adjust_customer(db)

        return customer_id

#function to print_selected_user
def print_selected_customer(customer_id):
    """
    Print customer you selected by customer_id
    """
    # print the selected CUSTOMER
    db.cursor.execute("SELECT * FROM customers WHERE id=?", (customer_id,))
    rows = db.cursor.fetchall()
    print('-' * 50)
    print('customer ID - customer_name - customer_website - customer_phone - vat_number')
    print('-' * 50)
    for row in rows:
        print('| ', end='')
        for i in row:
            print(i, end=' | ')
        print('')
    print('-' * 50)
    




def adjust_row(customer_id):
    """
    Enter the customer_id of the customer that needs to be adjusted.
    Enter the new details for this customer
    """
    customer_name = cs50.get_string("Enter the customer name: ")
    customer_website = input("Enter the customer website: ")
    customer_phone = input("Enter the customer phone number: ")
    vat_number = input("Enter the vat number: ")

    # Update the row in the database
    c = db.cursor
    c.execute("UPDATE customers SET customer_name=?, customer_website=?, customer_phone=?, vat_number=? WHERE id=?",
              (customer_name, customer_website, customer_phone, vat_number, customer_id))
    db.sqliteConnection.commit()
    print("Customer details updated successfully!")


def adjust_column(customer_id):
    """
    Adjust 1 column of a customer by entering the column name
    Then enter the new detail
    """
    # Query the database to get a list of column names in the CUSTOMERS table
    c = db.cursor
    c.execute("PRAGMA table_info(customers)")
    column_names = [column_info[1] for column_info in c.fetchall()]

    # Ask for the column to be adjusted
    column = input("Enter the column name to be adjusted: ")
    while column not in column_names:
        print("Invalid column name. Please try again.")
        column = input("Enter the column name to be adjusted: ")

    # Update the column in the database
    value = input("Enter the new value: ")
    c.execute("UPDATE customers SET {}=? WHERE id=?".format(column), (value, customer_id))
    db.sqliteConnection.commit()
    print("Customer details updated successfully!")


#choose which want toch adjust row or column
def adjust_type_func(customer_id):
    """
    Chose if you want to adjust 1 column or the whole row.
    :return: row or column
    """
    adjust_type = cs50.get_int("Choose what do you want to adjust:"
                               "\n1.whole row "
                               "\n2.specific column "
                               "\nChoose: ")
    if adjust_type != 1 or adjust_type !=2:
        if adjust_type == 1:
            print_selected_customer(customer_id)
            adjust_row(customer_id)
            return adjust_type

        elif adjust_type == 2:

            print_selected_customer(customer_id)
            adjust_column(customer_id)
            return adjust_type

        else:
            print('Choose a valid number!')
            adjust_type_func(customer_id)

def more_adjustments():
    """
    Asks if they want to make more adjustements
    :return: row or column
    """
    more = cs50.get_int(
        ("Do you want to "
         "\n1. adjust row/column of the same customer  "
         "\n2. choose another customer  "
         "\n3. exit"
         "\nChoose: "))
    return more


def extra(customer_id,more):
    """
    Ask if user wants to adjust more columns or choose another row/customer
    """
    while True:
        if more == 1:  # adjust same customer
            adjust_type_func(customer_id)
            more_adjustments()
        elif more == 2:  # another row/customer
            adjust_customer(db)
            adjust_type_func(customer_id)
            more_adjustments()
        elif more == 3:
            break


def adjust_customer_run():
    """
    Connect to the database
    Adjust project details
    """
    customer_id = adjust_customer(db)
    adjust_type_func(customer_id)
    more = more_adjustments()
    extra(customer_id,more)