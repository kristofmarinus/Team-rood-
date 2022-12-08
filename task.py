import datetime

class Task():
    #initializing the variables
    #note: maybe we should make these instance variables instead of  class variables
    #also: how are we gonna handle None (Null) values? 
    #it might be interesting to set a trigger in the database to keep track off when a task changes
    _id = None   # this might have to be deleted... for adding a new Task maybe we should let the SQLite autoincrement do its thing instead 

    _FK_projectID = 0  # maybe 0 is a bad option here.. 
    _FK_userId = 0  #maybe this needs to be an instance variable.. not every task has a user assigned to it
    _date_added = None #look at this again later... datetime.datetime.now() in setter looks like best options
    _deadline = None #look at this again later.. not every task needs a deadline
    _description = ''
    _date_finished = None #look at this again later... not every task needs this
    _date_started = None #the date a task is started
    #_date_changed = None  #do we need to keep track of this? trigger in database seems like best option

    #getters and setters for all the attributes... 
    #note: date will be difficult... 
    @property
    def id(self):
        self._id = id
    
    @id.setter
    def id(self, value):
        #add validation.... 
        self._id = value

    #... getters and setters for the other attributes

    @property
    def fromSQL(self, value):
        """sets  the variables of an instance to the values from the database
        """
        pass
        #query to get the date from SQL
        #assing the variables to those values... 

    #function: to write TO SQL
    #note: if we define the pointer in main, how does that inherit? 
    def to_SQL(self):
        pass

 


#function to ADD a task
#should be two functions: get input + make task 

#funtion to CHANGE a task (like assign user)
#should be two functions: get input + change task 

