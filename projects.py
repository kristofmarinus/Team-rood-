import datetime
import database_functions as dbf
from inputs import get_input_item

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



    def write_project(self):
        """writes project to the database
        """
        try:
            sql_cmd = f"insert into projects (project_name, project_descr, fk_customer_id, project_date_added, project_deadline, project_finished) values ('{self.project_name}','{self.project_descr}', '{self.fk_customer_id}', '{self.project_date_added}', '{self.project_deadline}', '{self.project_finished}');"
            dbf.cursor.execute(sql_cmd)
            dbf.sqliteConnection.commit()
        except Exception as e:
            print(f'fout def.write_project: {e}')

    @staticmethod
    def delete_project(inp: int):
        """delete project from database

        Args:
            inp (int): id nr of project to be deleted
        """
        try:
            sql_cmd = f'delete from projects where id = {inp};'
            dbf.cursor.execute(sql_cmd)
            dbf.sqliteConnection.commit()
            print('project deleted')
        except Exception as e:
            print(f'fout: {e}')

    @staticmethod
    def show_projects(project_id=-1):
        """show all users
        """
        project_id = get_input_item("Enter 1 to show all users",
                                    1)
        try:
            if project_id == 1:
                sql_cmd = 'select * from projects;'
            dbf.cursor.execute(sql_cmd)
            rows = dbf.cursor.fetchall()
            print('-' * 50)
            print('project ID - project_name - project_descr - fk_customer_id - project_date_added - project_deadline - project_finished')
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


def create_project() -> Project:
    """

    Asks for information

    Returns:
        Project: the project
    """
    project_name = get_input_item('Give project name')
    project_descr = get_input_item('Give project description')
    fk_customer_id = get_input_item('Give customer id')
    project_date_added = get_input_item('Give date when project is added')
    project_deadline = get_input_item('Give deadline date of project')
    project_finished = get_input_item('Is project finished')
    return Project


def add_project():
    """
    adds a project to the projects list
    """
    project = create_project()
    project.write_project()


def delete_project():
    """asks user which id to delete,

    double check : yes/no

    deletes the project
    """
    Project.show_projects()
    inp = get_input_item("Select project id to delete", 1)
    check = get_input_item(f'WARNING: Delete is irreparable --- enter "y" --- if you wish still to delete the project{inp}')
    if check.strip().lower() == "y":
        Project.delete_project(inp)
        print(f'PROJECT with id:{inp} was DELETED')
    else:
        print('Deletion was UNDONE.')
    # UPDATE ALL TASKS WHICH DELETED ID = PROJECT ID


def adjust_project(dbf):
        #Print all the info of the table projects
        sql_cmd = 'select * from projects;'
        dbf.cursor.execute(sql_cmd)
        rows = dbf.cursor.fetchall()
        print('-' * 50)
        print('project ID - project_name - project_descr - fk_customer_id - project_date_added - project_deadline - project_finished')
        print('-' * 50)
        if len(rows) > 0:
            for row in rows:
                print('| ', end='')
                for i in row:
                    print(i, end=' | ')
                print('')
        else:
            print('geen gegevens gevonden')

        # Choose id of the user
        print('-' * 50)

        project_id = int(input("Enter the id of the project: "))

        # Do you want to adjust whole row or specific column
        adjust_type = int(input("\n1.whole row \n2.specific column \nWhat do you want to adjust: "))

        if adjust_type == 1:
            # Ask for all the details
            project_name = input("Enter the project name: ")
            project_descr = input("Enter the project description: ")
            email = input("Enter the email: ")
            website = input("Enter the website: ")

            # Update the row in the database
            c = dbf.cursor()
            c.execute("UPDATE users SET first_name=?, last_name=?, email=?, website=?, WHERE id=?",
                      (fname, lname, email,website, user_id))
            dbf.commit()
            print("User details updated successfully!")
        elif adjust_type == 2:
            # Ask for the column to be adjusted
            column = input("Enter the column name to be adjusted: ")
            value = input("Enter the new value: ")

            # Update the column in the database
            c = dbf.cursor()
            c.execute("UPDATE users SET {}=? WHERE id=?".format(column), (value, user_id))
            dbf.commit()
            print("User details updated successfully!")


def adjust_user_run():
    # Connect to the database

    while True:
        # Adjust user details
        adjust_user(dbf)

        # Ask if user wants to adjust more column or choose another row/user
        more = int(
            input("Do you want to 1. adjust more column of the user or 2. choose another row/user or 3. exit: "))
        if more == 1:
            continue
        elif more == 2:
            continue
        elif more == 3:
            break
