import datetime
import database_functions as dbf

class User():

    _id = 'aap'
    _user_name = None

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
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        if value is not None:
            self._user_name = value

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
            self.id = dbf.give_field('users', id, 'id')
            self.user_name = dbf.give_field('users', id, 'user_name')
            

        except Exception as e:
            print(f'error in module from_sql : {e}')

    def to_SQL(self):
        pass

    def __str__(self):
        return self.description