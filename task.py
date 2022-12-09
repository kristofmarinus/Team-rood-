import datetime
import database_functions as dbf

class Task():
    #initializing the variables
    #note: maybe we should make these instance variables instead of  class variables
    #also: how are we gonna handle None (Null) values? 
    #it might be interesting to set a trigger in the database to keep track off when a task changes
    _id = 'aap'  # this might have to be deleted... for adding a new Task maybe we should let the SQLite autoincrement do its thing instead 

    _FK_projectID = None  # maybe 0 is a bad option here.. 
    _FK_userId = None  #maybe this needs to be an instance variable.. not every task has a user assigned to it
    _date_added = None #look at this again later... datetime.datetime.now() in setter looks like best options
    _deadline = None #look at this again later.. not every task needs a deadline
    _description = None
    _date_finished = None #look at this again later... not every task needs this
    _date_started = None #the date a task is started
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
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value is not None:
            self._description = value


    #... getters and setters for the other attributes



    @property
    def fromSQL(self):
        """sets  the variables of an instance to the values from the database
        """
        try: 
            self.description = dbf.show_field('tasks', 1, 'task_started_on')

        except Exception as e:
            print(e)
        #query to get the date from SQL
        #assing the variables to those values... 

    #function: to write TO SQL
    #note: if we define the pointer in main, how does that inherit? 
    def to_SQL(self):
        pass

    def __str__(self):
        return self.description

 


#function to ADD a task
#should be two functions: get input + make task 

#funtion to CHANGE a task (like assign user)
#should be two functions: get input + change task 

