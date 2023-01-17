import databaseconnection as db
from inputs import get_input_item
from src import cs50
import datetime
import database_functions as dbf
import sqlite3
from baseclass import BaseClass


class Project(BaseClass):
    __project_name = ""
    __project_descr = ""
    __fk_customer_id = ""
    __project_date_added = ""
    __project_deadline = ""
    __project_finished = "none"

    def __init__(self, project_name: str, project_descr: str):
        self.__project_name = project_name
        self.__project_descr = project_descr

    @property
    def project_name(self) -> str:
        return self.__project_name

    @project_name.setter
    def project_name(self, value):
        #note: setting project_name to None/Null is not allowed
        if value is None: 
            raise TypeError("project_name can not be None/Null")
        else: 
            try:
                self.__project_name = str(value)
            except: 
                raise TypeError('project_name has to be a string, or a type that can be converted to a string')


    @property
    def project_descr(self) -> str:
        return self.__project_descr

    @project_descr.setter
    def project_descr(self, value):
        #note: setting project_descr to None/Null is not allowed
        if value is None: 
            raise TypeError("project_descr can not be None/Null")
        else: 
            try:
                self.__project_descr = str(value)
            except: 
                raise TypeError('project_descr has to be a string, or a type that can be converted to a string')

    @property
    def fk_customer_id(self) -> int:
        return self.__fk_customer_id

    @fk_customer_id.setter
    def fk_customer_id(self, value: int):
        #note: setting fk_customer_id to None is not allowed
        try:
            value = int(value)
            if value > 0:
                self.__fk_customer_id = value
            else: 
                raise ValueError('fk_customer_id has to be positive')

        except: 
            raise TypeError('fk_customer_id has to be an integer, or a type that can be converted to an integer')


    @property
    def project_date_added(self):
        if isinstance(self.__project_date_added, datetime.date):
            return super().date_to_str(self.__project_date_added)
        elif self.__project_date_added is None:
            return None
        else:
            raise TypeError('date attribute is in wrong type')


    @project_date_added.setter
    def project_date_added(self, value):
        if isinstance(value, datetime.date):
            self.__project_date_added = value
        elif isinstance(value, str):
            self.__project_date_added = super().str_to_date(value)
        elif value is None:
            self.__project_date_added = None
        else:
            raise TypeError('date is in wrong type')


    @property
    def project_deadline(self):
        if isinstance(self.__project_deadline, datetime.date):
            return super().date_to_str(self.__project_deadline)
        elif self.__project_deadline is None:
            return None
        else:
            raise TypeError('date paramater is in wrong type')

    @project_deadline.setter
    def project_deadline(self, value):
        if isinstance(value, datetime.date):
            self.__project_deadline = value
        elif isinstance(value, str):
            self.__project_deadline = super().str_to_date(value)
        elif value is None:
            self.__project_deadline = None
        else:
            raise TypeError('date is in wrong type')

    @property
    def project_finished(self):
        return self.__project_finished

    @project_finished.setter
    def project_finished(self, value):
        try:
            self.__project_finished = (value)
        except: 
            raise TypeError('project_finished has to be a string, or a type that can be converted to a string')


    def write_project(self):
        """writes project to the database
        """
        try:
            sql_cmd = f"insert into projects (project_name, project_descr, fk_customer_id, project_date_added, project_deadline, project_finished) values ('{self.project_name}','{self.project_descr}', '{self.fk_customer_id}', '{self.project_date_added}', '{self.project_deadline}', '{self.project_finished}');"
            db.cursor.execute(sql_cmd)
            db.sqliteConnection.commit()
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
            db.cursor.execute(sql_cmd)
            db.sqliteConnection.commit()
            print('project deleted')
        except Exception as e:
            print(f'fout: {e}')
    
    @staticmethod
    def show_projects():
        """show all projects
        """
        """voorstel: 
        dbf.print_table("projects", dbf.give_table_filtered('projects'))
        """
        project_id = get_input_item("Enter 1 to show all projects",
                                    1)
        #Add a feature to show projects from X-ids to Y-ids.
        def show_projects_2(project_id):
            try:
                if project_id == 1:
                    sql_cmd = 'select * from projects;'
                db.cursor.execute(sql_cmd)
                rows = db.cursor.fetchall()
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
        show_projects_2(project_id)


def create_project() -> Project:
    """

    Asks for information

    Returns:
        Project: the project
    """
    project_name = get_input_item('Give project name: ')
    project_descr = get_input_item('Give project description: ')
    fk_customer_id = get_input_item('Give customer id: ')
    project_date_added = get_input_item('Give date when project was added: ')
    project_deadline = get_input_item('Give deadline: ')
    project_finished = get_input_item('Is project finished? (enter "yes" or "no"): ').strip().lower()
    project = Project(project_name, project_descr)
    project.fk_customer_id = fk_customer_id
    project.project_date_added = project_date_added
    project.project_deadline = project_deadline
    project.project_finished = project_finished
    return project


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
        print(f'Project with id:{inp} was DELETED')
    else:
        print('Deletion was UNDONE.')
        # UPDATE ALL TASKS WHICH DELETED ID = PROJECT ID


def adjust_project(db):

        def print_all():
            """
            Print all the info of the table projects
            return: prints all the projects
            """
            sql_cmd = 'select * from projects;'
            db.cursor.execute(sql_cmd)
            rows = db.cursor.fetchall()
            print('-' * 50)
            print('project ID - project_name - project_descr - fk_customer_id - project_date_added - project_deadline - project_finished')
            print('-' * 50)
            if len(rows) > 0:
                for row in rows:
                    print('| ', end='')
                    for i in row:
                        print(i, end=' | ')
                    print('')
                print('-' * 50)
            else:
                print('geen gegevens gevonden')
        print_all()

        # Choose id of the project
        project_id = cs50.get_int("Enter the id of the project: ")

        #cheking if the id of the project exists
        def id_exists(project_id):
            db.cursor.execute("SELECT * FROM projects WHERE id=?", (project_id,))
            result = db.cursor.fetchone()
            if result:
                return True
            else:
                return False

        # IF given id NOT exists restart the main function -> adjust_project()


        #if it is ok then print the project details
        if id_exists(project_id):
            return project_id

        if id_exists(project_id) is False:
            print("ID does not exist in the table")
            print("Choose another one")
            adjust_project(db)

        return project_id

#function to print_selected_project
def print_selected_project(project_id):
    """
    voorstel: volledige functie vervangen door: 
    dbf.print_record("projects",dbf.give_record_filtered("projects", project_id), dbf.get_justify_values("projects" ,dbf.give_record_filtered("projects", project_id)))
    """
    # print the selected PROJECT
    db.cursor.execute("SELECT * FROM projects WHERE id=?", (project_id,))
    rows = db.cursor.fetchall()
    print('-' * 50)
    print('project ID - project_name - project_descr - fk_customer_id - project_date_added - project_deadline - project_finished')
    print('-' * 50)
    for row in rows:
        print('| ', end='')
        for i in row:
            print(i, end=' | ')
        print('')
    print('-' * 50)
    




def adjust_row(project_id):
    # Ask for all the details
    project_name = cs50.get_string("Enter the project name: ")
    project_descr = cs50.get_string("Enter the project description: ")
    fk_customer_id = input("Enter the customer id: ")
    project_date_added = input("Enter the date when project was added: ")
    project_deadline = input("Enter the deadline: ")
    project_finished = input("Enter if project is finished: ")

    # Update the row in the database
    c = db.cursor
    c.execute("UPDATE projects SET project_name=?, project_descr=?, fk_customer_id=?, project_date_added=?, project_deadline=?, project_finished=? WHERE id=?",
             (project_name, project_descr, fk_customer_id, project_date_added, project_deadline, project_finished, project_id))
    db.sqliteConnection.commit()


def adjust_column(project_id):
    # Query the database to get a list of column names in the PROJECTS table
    c = db.cursor
    c.execute("PRAGMA table_info(projects)")
    column_names = [column_info[1] for column_info in c.fetchall()]

    # Ask for the column to be adjusted
    column = input("Enter the column name to be adjusted: ")
    while column not in column_names:
        print("Invalid column name. Please try again.")
        column = input("Enter the column name to be adjusted: ")

    # Update the column in the database
    value = input("Enter the new value: ")
    c.execute("UPDATE projects SET {}=? WHERE id=?".format(column), (value, project_id))
    db.sqliteConnection.commit()
    print("Project details updated successfully!")





#choose which want toch adjust row or column
def adjust_type_func(project_id):
    """
        # Do you want to adjust whole row or specific column
    :return: row or column
    """
    adjust_type = cs50.get_int("Choose what do you want to adjust:"
                                "\n1.whole row "
                                "\n2.specific column "
                                "\nChoose: ")
    if adjust_type != 1 or adjust_type !=2:
        if adjust_type == 1:
            print_selected_project(project_id)
            adjust_row(project_id)
            return adjust_type

        elif adjust_type == 2:

            print_selected_project(project_id)
            adjust_column(project_id)
            return adjust_type

        else:
            print('Choose a valid number!')
            adjust_type_func(project_id)

def more_adjustments():
    more = cs50.get_int(
        ("Do you want to "
        "\n1. adjust row/column of the same project  "
        "\n2. choose another project  "
        "\n3. exit"
        "\nChoose: "))
    return more


def extra(project_id,more):
    while True:
        # Ask if user wants to adjust more column or choose another row/project
        if more == 1:  # adjust same project
            adjust_type_func(project_id)
            more_adjustments()
        elif more == 2:  # another row/project
            adjust_project(db)
            adjust_type_func(project_id)
            more_adjustments()
        elif more == 3:
            break


def adjust_project_run():
    # Connect to the database
    # Adjust project details
        project_id = adjust_project(db)
        adjust_type_func(project_id)
        more = more_adjustments()
        extra(project_id,more)

