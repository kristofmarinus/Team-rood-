import database_functions as dbf
import databaseconnection as db
from baseclass import BaseClass
import datetime
import sqlite3
from get_input import get_input



class Task(BaseClass):
    # initializing the variables
    # note: maybe we should make these instance variables instead of  class variables
    # also: how are we gonna handle None (Null) values?
    # it might be interesting to set a trigger in the database to keep track off when a task changes
    _tablename = 'tasks'

    _id = None #not Null constraint in database
    _task_descr = None #not Null constraint in database
    _fk_project_id = None #not Null constraint in database
    _fk_user_id = None  
    _task_date_added = None 
    _task_deadline = None 
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

    @staticmethod
    def delete_tasks_by_project_id(inp: int):
        try:
            sql_cmd = f"DELETE FROM tasks WHERE fk_project_id={inp};"
            db.cursor.execute(sql_cmd)
            db.sqliteConnection.commit()
            print(f'Deleted all tasks associated with project id: {inp}')
        except Exception as e:
            print(f'fout def.delete_tasks_by_project_id: {e}')
        
    def to_db(self):
        """writes a task to DB. (SQL update for existing, changed, task and SQL insert for a new task)
        """
        # we handle new records, and updating existing records
        # if id is None: means it's a new task (not previously read from database)
        # so to_db will create a new record (INSERT statement)
        if self._id is None: 
            try:
                query1 = f'insert into {self._tablename} '
                query2= f'(task_descr, fk_user_id, fk_project_id, task_date_added, task_deadline, task_progress, task_started_on, task_finished_on) '
                query3 = f'values '
                query4 = f'("{self._task_descr}" , {self._fk_user_id} , {self._fk_project_id}, "{self.task_date_added}", "{self.task_deadline}", {self._task_progress},  "{self.task_started_on}", "{self.task_finished_on}");'.replace('"None"', 'Null').replace('None', 'Null')
                query = query1 + query2 + query3 + query4
                count = db.cursor.execute(query)
                db.sqliteConnection.commit()
            except sqlite3.Error as error:
                print('Error occured - ', error)
        #if ID is not none: means the record most likely CAME from the database or existing record has to be changed. so an UPDATE statement is used
        if not self._id is None: 
            try:
                #note: the id is NOT updated
                query1 = f'update {self._tablename} '
                query2 = f'set task_descr = "{self._task_descr}", fk_user_id = {self._fk_user_id}, fk_project_id = {self._fk_project_id}, task_date_added = "{self.task_date_added}", '
                query3 = f'task_deadline = "{self.task_deadline}", task_progress = "{self.task_progress}", task_started_on = "{self.task_started_on}", task_finished_on = "{self.task_finished_on}" '
                query4 = f'where id = {self._id}'
                query_together = query1 + query2 + query3 + query4
                #cleaning up the query for SQL synstax:
                query = query_together.replace('"None"', 'Null').replace('None', 'Null')
                count = db.cursor.execute(query)
                db.sqliteConnection.commit()
            except sqlite3.Error as error:
                print('Error occured - ', error)


    def delete(self):
        """handles deleting a task"""
        try:
            sql_cmd = f'delete from tasks where id = {self.id};'
            db.cursor.execute(sql_cmd)
            db.sqliteConnection.commit()
            print('Task deleted')
        except Exception as e:
            print(f'error deleting task: {e}')


    def __str__(self):
        return self.__dict__()



def create_task():
    """handles user creating a new task. does not ask for EVERY attribute, only the "basic" ones. User can edit the task later. 
    """
    print('Creating a new task! Please give the required info: ')
    #initialize a new (empty) task instance
    new_task = Task()
    new_task.task_descr = input('please give the task description: ')
    #get project_id for the task (project_id can not be None): 
    while True: 
        print('A task has to be assigned to a project. Here is the list of projects: ')
        #print the table of all projects: 
        dbf.print_table('projects', dbf.give_table_filtered('projects'))
        #get input for the new project (has to be an integer)
        project = get_input('Give the project to assign this task to: ', 1)
        # test if the input value is the id of an existing project: 
        list_project_id = dbf.give_id_table('projects')
        if project in list_project_id:
            new_task.fk_project_id = project
            break 
        else: 
            print("-" * 35)
            print("-" * 35)
            print('invalid choice! pleace choose one of the existing projects!')
    #(optional): get user assigned to task
    while True:
        print('Do you want to assign a user to this project? if not: type NO, if yes: type YES')
        input_dialog = get_input('Yes/No : ').lower().strip()
        if input_dialog == "no":
            new_task.fk_user_id = None
            break
        if input_dialog == "yes":
            print('you chose to assing a user. This is a list of all the users: ')
            dbf.print_table("users", dbf.give_table_filtered("users"))
            #loop to get the input, and check if input is an ID that is in the table "users"
            while True:
                print()
                input_id = get_input('give id of the user you want to assing this task to: ', 1)
                list_user_id = dbf.give_id_table("users")
                if input_id in list_user_id:
                    new_task.fk_user_id = input_id
                    break
                else:
                    print("-" * 35)
                    print("-" * 35)
                    print('invalid choice! pleace choose one of the existing users!')
        break
    #(optional): get a deadline for the task
    while True: 
        print('Do you want to assign a deadline to this project? if not: type NO, if yes: type YES')
        input_dialog = get_input('Yes/No : ').lower().strip()
        if input_dialog == "no": #ad getter setter for deadline
            new_task.task_deadline = None
            break
        if input_dialog == "yes":
            input_deadline = get_input('Please give the deadline in format: YYYY/MM/DD: ')
            try: 
                new_task.task_deadline = new_task.str_to_date(input_deadline)
                break
            except: 
                print('date format was incorrect! please use YYYY/MM/DD')
    #dialog for saving the task: 
    while True: 
        input_dialog = get_input('you have completed the input for this task. Do you want to save it? YES/NO: ').lower().strip()
        if input_dialog == 'yes':
            #save to database
            new_task.to_db()
            break
        elif input_dialog == 'no':
            break
        else: 
            print('invalid input... please try again. ')


def select_task()->Task:
    """handles user selecting a task

    Returns:
        Task: the task the user selected
    """
    #print table with all the tasks: 
    print("SELECT A TASK:")
    print("These are all the tasks: ")
    dbf.print_table("tasks", dbf.give_table_filtered("tasks"))
    #get user input: 
    while True: 
        task_choice = get_input('give the ID of the task you choose: ', 1)
        #test if user input is in the list of tasks: 
        list_task_id = dbf.give_id_table('tasks')
        if task_choice in list_task_id:
            chosen_task = Task()
            #get property values from database
            chosen_task.from_db = task_choice
            return chosen_task
        else: 
            print("invalid id... please choose an id from the list! ")


def change_task():
    """handles user changing a task
    """
    print("CHANGE A TASK:")
    #select the task:
    task = select_task()
    print("the task you want to change: ")
    #print the entire record (so all columns, not the "filtered" list)
    dbf.print_record("tasks", dbf.give_record("tasks", task.id), [], False, False)
    # we go over all the parameters and ask if the user wants to change them: 
    # (task ID, task date_added and task date_changed can not be changed manualy by user)d
    #change description
    while True: 
        input_dialog = get_input("Do you want to change the task description? Y/N: ").lower().strip()
        if input_dialog == "n":
            break
        if input_dialog == "y":
            new_value = get_input('Give the new description: ')
            #handle the validition by using the setter
            try:
                task.task_descr = new_value
                break
            except Exception as e:
                print(f'input is in wrong format. Exception: {e}')
    #change project_id
    while True: 
        input_dialog = get_input("Do you want to change the project ID? Y/N: ").lower().strip()
        if input_dialog == "n":
            break
        if input_dialog == "y":
            #print the table of all projects: 
            print("this is a list of all the projects: ")
            dbf.print_table('projects', dbf.give_table_filtered('projects'))
            #get input: 
            new_value = get_input('Give the new project ID: ',1)
            #test that the input is a project id: 
            list_project_id = dbf.give_id_table('projects')
            if new_value in list_project_id: 
                #handle the validation by using the setter
                try:
                    task.fk_project_id = new_value
                    break
                except Exception as e:
                    print(f'input is in wrong format. Exception: {e}')
            else:
                print('that is not a valid project ID, please choose one from the list')
    #change user_id (None value is allowed)
    while True: 
        input_dialog = get_input("Do you want to change the user_id? Y/N: ").lower().strip()
        if input_dialog == "n":
            break
        if input_dialog == "y":
            #print the table of all users: 
            print("this is a list of all the users: ")
            dbf.print_table('users', dbf.give_table_filtered('users'))
            #get input: 
            new_value = get_input('Give the new project ID or give "0" for "None": ',1)  
            #get list containing all user id's
            list_id = dbf.give_id_table('users')          
            #if input is "0", set to None:
            if new_value == 0:
                task.fk_user_id = None
                break
            #test that the input is a user id: 
            elif new_value in list_id: 
                #handle the validation by using the setter
                try:
                    task.fk_user_id = new_value
                    break
                except Exception as e:
                    print(f'input is in wrong format. Exception: {e}')
            else:
                print('that is not a valid user ID, please choose one from the list')
    #change task deadline (None value is allowed)
    while True: 
        input_dialog = get_input("Do you want to change the task deadline? Y/N: ").lower().strip()
        if input_dialog == "n":
            break
        if input_dialog == "y":
            new_value = get_input('Give the new deadline in format YYYY/MM/DD or type "None" for None: ')
            
            if new_value.lower().strip() == "none":
                try: 
                    task.task_deadline = None
                    break
                except Exception as e: 
                    print(f'error setting task deadline to None. Exception: {e}') 
            else: 
                #handle the validation by using the setter
                try:
                    task.task_deadline = new_value
                    break
                except Exception as e:
                    print(f'input is in wrong format. Exception: {e}')    
    #change task progress (None value is allowed)
    while True: 
        input_dialog = get_input("Do you want to change the task progress? Y/N: ").lower().strip()
        if input_dialog == "n":
            break
        if input_dialog == "y":
            new_value = get_input('Give the new task progress (number between 0 and 100) or type "None" for None: ').lower().strip()
            #handle the validation by using the setter
            if new_value == 'null':
                task.task_progress = None
                break
            else:
                try:
                    task.task_progress = new_value
                    break
                except Exception as e:
                    print(f'input is in wrong format. Exception: {e}')   
    #change task started_on date (None value is allowed)
    while True: 
        input_dialog = get_input("Do you want to change the task started_on date? Y/N: ").lower().strip()
        if input_dialog == "n":
            break
        if input_dialog == "y":
            new_value = get_input('Give the new task started_on date in format YYYY/MM/DD or type "None" for None: ')            
            if new_value.lower().strip() == "none":
                try: 
                    task.task_started_on = None
                    break
                except Exception as e: 
                    print(f'error setting task started_on to None. Exception: {e}') 
            else: 
                #handle the validition by using the setter
                try:
                    task.task_started_on = new_value
                    break
                except Exception as e:
                    print(f'input is in wrong format. Exception: {e}')    
    #change task finished_on date (None value is allowed)
    while True: 
        input_dialog = get_input("Do you want to change the task finished_on date? Y/N: ").lower().strip()
        if input_dialog == "n":
            break
        if input_dialog == "y":
            new_value = get_input('Give the new task finished_on date in format YYYY/MM/DD or type "None" for None: ')            
            if new_value.lower().strip() == "none":
                try: 
                    task.task_finished_on = None
                    break
                except Exception as e: 
                    print(f'error setting task finished_on to None. Exception: {e}') 
            else: 
                #handle the validition by using the setter
                try:
                    task.task_finished_on = new_value
                    break
                except Exception as e:
                    print(f'input is in wrong format. Exception: {e}')    
    #input stage is complete... now we ask the user if he wants to save the changes or not?
    while True:
        input_user = get_input("you have finished the input for change-task... do you want to save the changes? YES/NO: ").lower().strip()
        if input_user == 'no':
            break
        elif input_user == 'yes':
            #write task to database:
            task.to_db()
            break


def delete_task():
    """handles deleting a task from database. calls self.delete() after a user dialog to select the task
    """
    print("DELETE A TASK:")
    print("SELECT A TASK TO DELETE:")
    task_delete = select_task()
    print("the task you selected to delete is: ")
    #print the entire record (so all columns, not the "filtered" list)
    dbf.print_record("tasks", dbf.give_record("tasks", task_delete.id), [], False, False)
    while True: 
        are_you_sure = get_input("are you sure you want to delete this task? YES/NO: ").lower().strip()
        if are_you_sure == "no":
            break
        elif are_you_sure == "yes":            
            try:
                #delete the task
                task_delete.delete()
                break
            except Exception as e:
                print(f'fout: {e}')
                break
        else: 
            print("invalid input... please ty again... ")

def print_all_unfinished_tasks():
    """handles printing all unfinished (open) tasks. a task is unfinished until (date) task_finished_on is filled in in database
    """
    print('THESE ARE ALL OPEN TASKS: ')  
    #get query result: 
    try: 
        query = 'select * from tasks where task_finished_on is Null;'
        count = db.cursor.execute(query)
        result = db.cursor.fetchall()
    except sqlite3.Error as error:
        print('Error occured - ', error)
    if len(result) == 0:
        print('lege tabel!')
    #filter result (only the visible columns remain)
    result_filtered = dbf.filter_result("tasks", result)
    #print table: 
    dbf.print_table("tasks", result_filtered)


def print_all_finished_tasks():
    """handles printing all finished (open) tasks. a task is unfinished until (date) task_finished_on is filled in in database
    """
    print('THESE ARE ALL FINISHED TASKS: ')  
    #get query result: 
    try: 
        query = 'select * from tasks where task_finished_on is not Null;'
        count = db.cursor.execute(query)
        result = db.cursor.fetchall()
    except sqlite3.Error as error:
        print('Error occured - ', error)
    if len(result) == 0:
        print('lege tabel!')
    #filter result (only the visible columns remain)
    result_filtered = dbf.filter_result("tasks", result)
    #print table: 
    dbf.print_table("tasks", result_filtered)
                    

def main():
    print_all_unfinished_tasks()


if __name__ == '__main__':
    main()
