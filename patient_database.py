import sqlite3

class PatientDatabase:
    def __init__(self):
        self.patient_db_name = "patients"

    def create_patient_db(self):
        con = sqlite3.connect(self.patient_db_name)
        return con

    def create_table_detail(self):
        '''
        This method will create a table "detail" if does not exist.
        '''
        # connection
        con = self.create_patient_db()
        # cursor
        cur = con.cursor()

        # create table "details" if does not exist
        cur.execute(""" CREATE TABLE if not exists detail(
                                                            name text,
                                                            dob text,
                                                            phone text
                                                            )"""
                    )

        # save
        con.commit()
        con.close()

    def insert_in_table_detail(self, name, dob, phone):
        # create table if does not exist
        self.create_table_detail()

        # connection
        con = self.create_patient_db()

        # cursor
        cur = con.cursor()
        
        # data to be inserted into table "detail"
        data = [name, dob, phone]

        # insert in table "details"
        cur.execute(" INSERT INTO detail values(?, ? , ?)", data )

        con.commit()
        con.close()
        print("I am inside insert_in_table_detail")

    def display_from_table_detail(self):

        # connection
        con = self.create_patient_db()

        # cursor
        cur = con.cursor()

        res = cur.execute("SELECT name from detail")
        records = res.fetchall()

        con.close()

        return records

    
