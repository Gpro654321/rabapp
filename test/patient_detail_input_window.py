from kivy.uix.screenmanager import Screen
from kivymd.uix.pickers import MDDatePicker

from kivy.utils import platform


from patient_database import PatientDatabase

if platform == "android":
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


        if platform == "android":
            sendsms.send_remainders()
            vibrator.vibrate(10)

    # }}}

    #{{{ on_save1
    def on_save1(self, instance, value, date_range):
        # print(instance, value)
        self.ids.dob.text = value.strftime("%d-%m-%Y")
        # return value
    #}}}

    #{{{ on_save2
    def on_save2(self, instance, value, date_range):
        # print(instance, value)
        self.ids.dov.text = value.strftime("%d-%m-%Y")
        # return value
    #}}}

    #{{{ on_cancel 
    def on_cancel(self, instance, value):
        pass

    #}}}

    #{{{show_date_picker
    def show_date_picker(self, field):
        date_dialog = MDDatePicker()
        if (field == "dob"):
            date_dialog.bind(on_save = self.on_save1, on_cancel=self.on_cancel)
        if (field == "dov"):
            date_dialog.bind(on_save = self.on_save2, on_cancel=self.on_cancel)


        date_dialog.open()
    #}}}
