import datetime

class Task():
    #initializing the variables
    #note: maybe we should make these instance variables instead of  class variables
    #also: how are we gonna handle None (Null) values? 
    #it might be interesting to set a trigger in the database to keep track off when a task changes
    _id = None   # this might have to be deleted... for adding a new Task maybe we should let the SQLite autoincrement do its thing instead 

    _FK_projectID = 0
    _FK_userId = 0
    _date_added = None #look at this again later... datetime.datetime.now() in setter looks like best options
    _deadline = None #look at this again later.. not every task needs a deadline
    _description = ''
    _date_finished = None #look at this again later... not every task needs this
    _date_started = None #the date a task is started
    #_date_changed = None  #do we need to keep track of this? trigger in database seems like best option

    #getters and setters for all the attributes... 
    #note: date will be a difficult one

    @property
    def id(self):


    #add property "fromSQL"

    #add function: toSQL
    #note: if we define the pointer in main, how does that inherit? 

 


