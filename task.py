import database_functions as dbf
import databaseconnection as db
from baseclass import BaseClass
import datetime
import sqlite3


class Task(BaseClass):
    # initializing the variables
    # note: maybe we should make these instance variables instead of  class variables
    # also: how are we gonna handle None (Null) values?
    # it might be interesting to set a trigger in the database to keep track off when a task changes
    _tablename = 'tasks'

    _id = None  
    _fk_project_id = None 
    _fk_user_id = None  
    _task_date_added = None 
    _task_deadline = None 
    _task_descr = None
    _task_progress = None
    _task_started_on = None
    _task_finished_on = None

    #getters and setters for all the attributes... 
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value):
        # note: setting the ID to "none" is not allowed
        try: 
            value = int(value)
            if value > 0:
                self._id = value
            else:
                raise ValueError('id has to be positive')
        except: 
            raise TypeError('id has to be an integer, or a type that can be converted to an integer')

    @property
    def task_descr(self) -> str:
        return self._task_descr

    @task_descr.setter
    def task_descr(self, value):
        #note: setting task_descr to None/Null is not allowed
        if value is None: 
            raise TypeError("task_descr can not be None/Null")
        else: 
            try:
                self._task_descr = str(value)
            except: 
                raise TypeError('task_descr has to be a string, or a type that can be converted to a string')

    @property
    def fk_project_id(self) -> int:
        return self._fk_project_id

    @fk_project_id.setter
    def fk_project_id(self, value: int):
        #note: setting fk_project_id to None is not allowed
        try:
            value = int(value)
            if value > 0:
                self._fk_project_id = value
            else: 
                raise ValueError('fk_project_id has to be positive')

        except: 
            raise TypeError('fk_project_id has to be an integer, or a type that can be converted to an integer')


    @property
    def fk_user_id(self) -> int:
        return self._fk_user_id

    @fk_user_id.setter
    def fk_user_id(self, value):
        if value is None:
            self._fk_user_id = None
        else:
            try:
                value = int(value)
                if value > 0:
                    self._fk_user_id = value
                else: 
                    raise ValueError('fk_user_id has to be positive')
            except: 
                raise TypeError('fk_user_id has to be Null/none, and integer, or a type that can be converted to an integer')
        

    @property
    def task_date_added(self):
        if isinstance(self._task_date_added, datetime.date):
            return super().date_to_str(self._task_date_added)
        elif self._task_date_added is None:
            return None
        else:
            raise TypeError('date attribute is in wrong type')

    @task_date_added.setter
    def task_date_added(self, value):
        if isinstance(value, datetime.date):
            self._task_date_added = value
        elif isinstance(value, str):
            self._task_date_added = super().str_to_date(value)
        elif value is None:
            self._task_date_added = None
        else:
            raise TypeError('date is in wrong type')

    @property
    def task_deadline(self):
        if isinstance(self._task_deadline, datetime.date):
            return super().date_to_str(self._task_deadline)
        elif self._task_deadline is None:
            return None
        else:
            raise TypeError('date paramater is in wrong type')

    @task_deadline.setter
    def task_deadline(self, value):
        if isinstance(value, datetime.date):
            self._task_deadline = value
        elif isinstance(value, str):
            self._deadline = super().str_to_date(value)
        elif value is None:
            self._task_deadline = None
        else:
            raise TypeError('date is in wrong type')

    @property
    def task_progress(self) -> int:
        """progress is an integer [0 - 100]"""
        return self._task_progress

    @task_progress.setter
    def task_progress(self, value):
        if value is None: 
            self._task_progress = None
        else: 
            try: 
                value = int(value)
                if value >= 0 and value <= 100:
                    self._task_progress = value
                else: 
                    raise ValueError('task_progress has to be within [0,100]')
            except: 
                raise TypeError('task_progress has to be Null/None, an integer, or a type that can be converted to an integer')

    @property
    def task_started_on(self):
        if isinstance(self._task_started_on, datetime.date):
            return super().date_to_str(self._task_started_on)
        elif self._task_started_on is None:
            return None
        else:
            raise TypeError('date attribute is in wrong type')

    @task_started_on.setter
    def task_started_on(self, value):
        if isinstance(value, datetime.date):
            self._task_started_on = value
        elif isinstance(value, str):
            self._task_started_on = super().str_to_date(value)
        elif value is None:
            self._task_started_on = None
        else:
            raise TypeError('date is in wrong type')

    @property
    def task_finished_on(self):
        if isinstance(self._task_finished_on, datetime.date):
            return super().date_to_str(self._task_finished_on)
        elif self._task_finished_on is None:
            return None
        else:
            raise TypeError('date paramater is in wrong type')

    @task_finished_on.setter
    def task_finished_on(self, value):
        if isinstance(value, datetime.date):
            self._finished_on = value
        elif isinstance(value, str):
            self._task_finished_on = super().str_to_date(value)
        elif value is None:
            self._task_finished_on = None
        else:
            raise TypeError('date is in wrong type')

    @property
    def from_db(self):
        """sets  the variables of an instance to the values from the database
        """
        try:
            pass
        #query to get the date from SQL
        #assing the variables to those values... 

        except Exception as e:
            print(e)
        # query to get the date from SQL
        # assing the variables to those values...
 

    @from_db.setter
    def from_db(self, id: int):
        """sets the attributes to the values from the db. 
        for example "new_task.from_db = 15" will set the attribute values of a task called new_task to the values from the database
        Args:
            id (int): the id of the record
        """
        try:
            self.id = dbf.give_field('tasks', id, 'id')
            self.task_descr = dbf.give_field('tasks', id, 'task_descr')
            self.fk_user_id = dbf.give_field('tasks', id, 'fk_user_id')
            self.fk_project_id = dbf.give_field('tasks', id, 'fk_project_id')
            self.task_date_added = dbf.give_field('tasks', id, 'task_date_added')
            self.task_deadline = dbf.give_field('tasks', id, 'task_deadline')
            self.task_progress = dbf.give_field('tasks', id, 'task_progress')
            self.task_started_on = dbf.give_field('tasks', id, 'task_started_on')
            self.task_finished_on = dbf.give_field('tasks', id, 'task_finished_on')

        except Exception as e:
            print(f'error in module from_db : {e}')

    def to_db(self):
        # we handle new records, and updating existing records
        # if id is None: means it's a new task (not previously read from database)
        # so to_db will create a new record (INSERT statement)
        if self.id is None: 
            try:
                query1 = f'insert into {self._tablename} '
                query2= f'(task_descr, fk_user_id, fk_project_id, task_date_added, task_deadline, task_progress, task_started_on, task_finished_on) '
                query3 = f'values '
                query4 = f'("{self.task_descr}" , {self.fk_user_id} , {self.fk_project_id}, "{self.task_date_added}", "{self.task_deadline}", {self.task_progress},  "{self.task_started_on}", "{self.task_finished_on}");'.replace('"None"', 'Null').replace('None', 'Null')
                query = query1 + query2 + query3 + query4
                count = db.cursor.execute(query)
                db.sqliteConnection.commit()
            except sqlite3.Error as error:
                print('Error occured - ', error)
        #if ID is not none: means the record most likely CAME from the database or existing record has to be changed. so an UPDATE statement is used
        if not self.id is None: 
            try:
                #note: the id is NOT updated
                query1 = f'update {self._tablename} '
                query2 = f'set task_descr = "{self.task_descr}", fk_user_id = {self.fk_user_id}, fk_project_id = {self.fk_project_id}, task_date_added = "{self.task_date_added}", '
                query3 = f'task_deadline = "{self.task_deadline}", task_progress = "{self.task_progress}", task_started_on = "{self.task_started_on}", task_finished_on = "{self.task_finished_on}" '
                query4 = f'where id = {self.id}'
                query_together = query1 + query2 + query3 + query4
                #cleaning up the query for SQL synstax:
                query = query_together.replace('"None"', 'Null').replace('None', 'Null')
                count = db.cursor.execute(query)
                db.sqliteConnection.commit()
            except sqlite3.Error as error:
                print('Error occured - ', error)


    def __str__(self):
        return self.__dict__()

# funtion to CHANGE a task (like assign user)
# should be two functions: get input + change task
def main():
    pass
   



if __name__ == '__main__':
    main()
