import datetime
import database_functions as dbf

class Project():

    _id = 'aap'
    _project_name = None
    _project_descr = None
    _fk_customer_id = None
    _project_date_added = None
    _project_deadline = None
    _project_finished = None

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
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        if value is not None:
            self._project_name = value

    @property
    def project_descr(self):
        return self._project_descr

    @project_descr.setter
    def project_descr(self, value):
        if value is not None:
            self._project_descr = value

     @property
    def fk_customer_id(self):
        return self._fk_customer_id

    @fk_customer_id.setter
    def fk_customer_id(self, value):
        if value is not None:
            self._fk_customer_id = value

     @property
    def project_date_added(self):
        return self.project_date_added

    @project_date_added.setter
    def project_date_added(self, value):
        if value is not None:
            self._project_date_added = value

     @property
    def project_deadline(self):
        return self._project_deadline

    @project_deadline.setter
    def project_deadline(self, value):
        if value is not None:
            self._project_deadline = value

     @property
    def project_finished(self):
        return self._project_finished

    @project_finished.setter
    def project_finished(self, value):
        if value is not None:
            self._project_finished = value

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
            self.id = dbf.give_field('projects', id, 'id')
            self.project_name = dbf.give_field('projects', id, 'project_name')
            self.project_descr = dbf.give_field('projects', id, 'project_descr')
            self.fk_customer_id = dbf.give_field('projects', id, 'fk_customer_id')
            self.project_date_added = dbf.give_field('projects', id, 'project_date_added')
            self.project_deadline = dbf.give_field('projects', id, 'project_deadline')
            self.project_finished = dbf.give_field('projects', id, 'project_finished')


        except Exception as e:
            print(f'error in module from_sql : {e}')

    def to_SQL(self):
        pass

    def __str__(self):
        return self.description