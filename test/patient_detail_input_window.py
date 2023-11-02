from kivy.uix.screenmanager import Screen


from patient_database import PatientDatabase
import sendsms
from plyer import vibrator

class PatientDetailInputWindow(Screen):
    pass


    # {{{ on_press_button
    def on_press_button(self, instance):
        
        patient_db = PatientDatabase()

        name  = self.ids.name.text
        dob = self.ids.dob.text
        dov = self.ids.dov.text
        phone = self.ids.phone.text

        # insert into table "detail"
        # since the method returns the lastrowid the value is stored in a variable
        patient_id = patient_db.insert_in_table_detail(name,dob,dov,phone)

        rec = patient_db.display_from_table_detail()
        print(rec)

        # insert into table "vacdates"
        patient_db.insert_in_table_vacdates(patient_id)

        rec2 = patient_db.display_from_table_vacdates()
        # rec2 = patient_db.display_from_table_vacdates_on_a_date('2023-11-03')
        print("From Vacdates")
        print(rec2)

        sendsms.send_remainders()
        vibrator.vibrate(10)

    # }}}
