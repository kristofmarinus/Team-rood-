import datetime
import database_functions as dbf

class Customer():

    _id = 'aap'
    _customer_name = None
    _customer_website = None
    _customer_phone = None
    _vat_number = None

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError('id moet een integer zijn')
        elif value >0: 
            self._id = value
        else: 
            raise ValueError('id moet positief zijn')

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        if value is not None:
            self._customer_name = value

    @property
    def customer_website(self):
        return self._customer_website

    @customer_website.setter
    def customer_website(self, value):
        if value is not None:
            self._customer_website = value

     @property
    def customer_phone(self):
        return self._customer_phone

    @customer_phone.setter
    def customer_phone(self, value):
        if value is not None:
            self._customer_phone = value

     @property
    def vat_number(self):
        return self._vat_number

    @vat_number.setter
    def vat_number(self, value):
        if value is not None:
            self._vat_number = value


    @property
    def from_sql(self):
        """sets  the variables of an instance to the values from the database
        """
        try: 
            pass

        except Exception as e:
            print(e)
        #query to get the date from SQL
        #assing the variables to those values... 

    #function: to write TO SQL
    #note: if we define the pointer in main, how does that inherit? 
    @from_sql.setter
    def from_sql(self, id:int):
        try: 
            self.id = dbf.give_field('customers', id, 'id')
            self.customer_name = dbf.give_field('customers', id, 'customer_name')
            self.customer_website = dbf.give_field('customers', id, 'customer_website')
            self.customer_phone = dbf.give_field('customers', id, 'customer_phone')
            self.vat_number = dbf.give_field('customers', id, 'vat_number')


        except Exception as e:
            print(f'error in module from_sql : {e}')

    def to_SQL(self):
        pass

    def __str__(self):
        return self.description