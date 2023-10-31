import sqlite3
import datetime

class PatientDatabase:
    def __init__(self):
        self.patient_db_name = "patients"

    #{{{ create_patient_db

    def create_patient_db(self):
        con = sqlite3.connect(self.patient_db_name)
        return con

    # }}}

    # {{{ create_table_detail

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

    # }}}

    #{{{ insert_in_table_detail

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

    # }}}

    #{{{ display_from_table_detail 

    def display_from_table_detail(self):

        # connection
        con = self.create_patient_db()

        # cursor
        cur = con.cursor()

        res = cur.execute("SELECT name from detail")
        records = res.fetchall()

        con.close()

        return records


    # }}}

    # {{{ create_table_vacdates 
    def create_table_vacdates(self):

        '''
        This method will create a table "vacdates" if does not exist.
        This table will have only 2 columns namely, phoneno and dateofvaccination
        '''
        # connection
        con = self.create_patient_db()
        # cursor
        cur = con.cursor()

        # create table "vacdates" if does not exist
        cur.execute(""" CREATE TABLE if not exists vacdates(
                                                            phone text,
                                                            date text
                                                            )"""
                    )

        # save
        con.commit()
        con.close()
    # }}}

    # {{{ insert_in_table_vacdates 

    def insert_in_table_vacdates(self, phone):
        '''
        This method when given a phone number shall call another method
        "calc_vac_dates" and the dates returned by that fucntion will be used here.
        '''
        # create table if does not exist
        self.create_table_vacdates()

        # connection
        con = self.create_patient_db()

        # cursor
        cur = con.cursor()

        # calculate the future dates
        dates = self.calc_vac_dates()
        
        for i in dates:
            # data to be inserted into table "vacdates"
            data = [phone, i]

            # insert in table "details"
            cur.execute(" INSERT INTO vacdates values(?, ?)", data )

        con.commit()
        con.close()
        print("I am inside insert_in_table_vacdates")

    # }}}

    # {{{ calc_vac_dates

    def calc_vac_dates(self):
        '''
        This function shall calculate the future dates of rabies vaccination 
        Assumption: today is the zeroth day
        '''
        zeroth_day = datetime.date.today()

        dates = []

        time_interval = [3,7,14,30]
        
        for i in time_interval:
            #Calculate the dates of the nth time_interval
            day_n = zeroth_day + datetime.timedelta(days=i)

            #Append the future date to dates
            dates.append(day_n)

        print("I am inside patient_database.calc_vac_dates")
        print(dates)
        return dates
        


    # }}}
    
    # {{{ display_from_table_vacdates

    def display_from_table_vacdates(self):

        # connection
        con = self.create_patient_db()

        # cursor
        cur = con.cursor()

        res = cur.execute("SELECT phone from vacdates")
        records = res.fetchall()

        con.close()

        return records
    # }}}

    # {{{ display from table vacdates on a particular date 
    def display_from_table_vacdates_on_a_date(self, date):

        # connection
        con = self.create_patient_db()

        # cursor
        cur = con.cursor()

        res = cur.execute("SELECT phone from vacdates WHERE date=(?)",[date])
        records = res.fetchall()

        con.close()

        return records

    # }}}
