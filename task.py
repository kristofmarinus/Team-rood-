import datetime
import database_functions as dbf
import sqlite3
import databaseconnection as db
from baseclass import BaseClass

class Task(BaseClass):
    #initializing the variables
    #note: maybe we should make these instance variables instead of  class variables
    #also: how are we gonna handle None (Null) values? 
    #it might be interesting to set a trigger in the database to keep track off when a task changes
    _tablename = 'tasks'
    _id = 'aap'  # this might have to be deleted... for adding a new Task maybe we should let the SQLite autoincrement do its thing instead 

    _fk_project_id = None  # maybe 0 is a bad option here.. 
    _fk_user_id = None  #maybe this needs to be an instance variable.. not every task has a user assigned to it
    _task_date_added = None #look at this again later... datetime.datetime.now() in setter looks like best options
    _task_deadline = None #look at this again later.. not every task needs a deadline
    _task_descr = None
    _task_progress = None
    _task_started_on = None
    _task_finished_on = None
    #_date_changed = None  #do we need to keep track of this? trigger in database seems like best option

    #getters and setters for all the attributes... 
    #note: date will be difficult... 
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
    def task_descr(self):
        return self._task_descr

    @task_descr.setter
    def task_descr(self, value):
        if value is not None:
            self._task_descr = value

    @property
    def fk_project_id(self)->int:
        return self._fk_project_id

    @fk_project_id.setter
    def fk_project_id(self, value:int):
        self._fk_project_id = value

    @property
    def fk_user_id(self)->int:
        return self._fk_user_id

    @fk_user_id.setter
    def fk_user_id(self, value):
        self._fk_user_id = value

    @property
    def task_date_added(self):
        return self._task_date_added

    @task_date_added.setter
    def task_date_added(self, value):
        self._task_date_added = value

    @property
    def task_deadline(self):
        return self._task_deadline

    @task_deadline.setter
    def task_deadline(self, value):
        self._task_deadline = value

    @property
    def task_progress(self):
        return self._task_progress

    @task_progress.setter
    def task_progress(self, value):
        self._task_progress = value
    
    @property
    def task_started_on(self):
        return self.task_started_on

    @task_started_on.setter
    def task_started_on(self, value):
        self._task_started_on = value

    @property
    def task_finished_on(self):
        return self.task_finished_on

    @task_finished_on.setter
    def task_finished_on(self, value):
        self._task_finished_on = value


    @property
    def from_db(self):
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
    @from_db.setter
    def from_db(self, id:int):
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
            print(f'error in module from_sql : {e}')

    def to_db(self):
        #nog uitbreiden: als self.id Null is: nieuwe record wegschrijven. als self.id niet Null is: bestaande record updaten
        #als we een nieuwe task aanmaken moeten we die GEEN id geven. Dat doet de database zelf bij het wegschrijven...
        try:
            query = f'insert into {self._tablename} (task_descr, fk_user_id, fk_project_id) values ("{self.task_descr}" , {self.fk_user_id} , {self.fk_project_id});'
            count = db.cursor.execute(query)
            db.sqliteConnection.commit()  
        except sqlite3.Error as error:
            print('Error occured - ', error)

    def __str__(self):
        return self.__dict__()





#funtion to CHANGE a task (like assign user)
#should be two functions: get input + change task 

