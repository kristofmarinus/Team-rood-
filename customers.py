import databaseconnection as db
from inputs import get_input_item
from src import cs50
import datetime
import database_functions as dbf

class Customer():

    _id = ""
    _name = ""
    _website = "none"
    _phone_number = ""
    _vat_number = "none"
    _email = "none"

    @property
    def _name(self):
        return self._name

    @_name.setter
    def _name(self, value):
        if value is not None:
            self._name = value

    @property
    def _website(self):
        return self._website

    @_website.setter
    def _website(self, value):
        if value is not None:
            self._website = value

    @property
    def _phone_number(self):
        return self._phone_number

    @_phone_number.setter
    def _phone_number(self, value):
        if value is not None:
            self._phone_number = value

    @property
    def vat_number(self):
        return self._vat_number

    @vat_number.setter
    def vat_number(self, value):
        if value is not None:
            self._vat_number = value

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


    def write_customer(self):
        """writes customer to the database
        """
        try:
            sql_cmd = f"insert into customers (name, website, phone_number, vat_number, email) values ('{self._name}','{self._website}', '{self._phone_number}', '{self._vat_number}', '{self._email}');"
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
        """voorstel: 
        dbf.print_table("customers", dbf.give_table_filtered('customers'))
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
                print('customer ID - name - website - phone_number - vat_number - email')
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
    name = get_input_item('Give name')
    website = get_input_item('Give website')
    phone_number = get_input_item('Give phone number')
    vat_number = get_input_item('Give vat number')
    email = get_input_item('Give email')
    Customer.website = website
    Customer.email = email
    return Customer


def add_customer():
    """
    adds a customer to the customer list
    """
    customer = create_customer()
    Customer.write_customer()


def delete_customer():
    """asks user which id to delete,

    double check : yes/no

    deletes the customer
    """
    Customer.show_customers()
    inp = get_input_item("Select customer id to delete", 1)
    check = get_input_item(f'WARNING: Delete is irreparable --- enter "y" --- if you wish still to delete the customer{inp}')
    if check.strip().lower() == "y":
        Customer.delete_customer(inp)
        print(f'CUSTOMER with id:{inp} was DELETED')
    else:
        print('Deletion was UNDONE.')


def adjust_customer(db):

        def print_all():
            """
            #Print all the info of the table customers
            :return: prints all the customers
            """
            sql_cmd = 'select * from customers;'
            db.cursor.execute(sql_cmd)
            rows = db.cursor.fetchall()
            print('-' * 50)
            print('customer ID - name - website - phone_number - vat_number - email')
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
        user_id = cs50.get_int("Enter the id of the customer: ")

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
    voorstel: volledige functie vervangen door: 
    dbf.print_record("customers",dbf.give_record_filtered("customers", customer_id), dbf.get_justify_values("customers" ,dbf.give_record_filtered("customers", customer_id)))
    """
    # print the selected CUSTOMER
    db.cursor.execute("SELECT * FROM customers WHERE id=?", (customer_id,))
    rows = db.cursor.fetchall()
    print('-' * 50)
    print('customer ID - name - website - phone_number - vat_number - email')
    print('-' * 50)
    for row in rows:
        print('| ', end='')
        for i in row:
            print(i, end=' | ')
        print('')
    print('-' * 50)
    




def adjust_row(customer_id):
    # Ask for all the details
    name = cs50.get_string("Enter the name: ")
    website = input("Enter the website: ")
    phone_number = input("Enter the phone number: ")
    vat_number = input("Enter the vat number: ")
    email = input("Enter the email: ")

    # Update the row in the database
    c = db.cursor
    c.execute("UPDATE customers SET name=?, website=?, phone_number=?, vat_number=?, email=? WHERE id=?",
              (name, website, phone_number, vat_number, email, customer_id))
    db.sqliteConnection.commit()
    print("User details updated successfully!")


def adjust_column(customer_id):
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
            # Do you want to adjust whole row or specific column
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
    more = cs50.get_int(
        ("Do you want to "
         "\n1. adjust row/column of the same customer  "
         "\n2. choose another customer  "
         "\n3. exit"
         "\nChoose: "))
    return more


def extra(customer_id,more):
    while True:
        # Ask if user wants to adjust more column or choose another row/customer
        if more == 1:  # adjust same customer
            adjust_type_func(customer_id)
            more_adjustments()
        elif more == 2:  # another row/customer
            adjust_customer(db)
            adjust_type_func(customer_id)
            more_adjustments()
        elif more == 3:
            break


def adjust_customer_run(customer_id):
    # Connect to the database
        # Adjust customer details
        cusotmer_id = adjust_customer(db)
        adjust_type_func(customer_id)
        more = more_adjustments()
        extra(customer_id,more)