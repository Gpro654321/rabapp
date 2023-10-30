from kivy.uix.screenmanager import Screen


from patient_database import PatientDatabase

class PatientDetailInputWindow(Screen):
    pass


    # {{{ on_press_button
    def on_press_button(self, instance):
        
        patient_db = PatientDatabase()

        name  = self.ids.name.text
        dob = self.ids.dob.text
        phone = self.ids.phone.text

        patient_db.insert_in_table_detail(name,dob,phone)

        print(name)
        print(dob)
        print(phone)
        
        rec = patient_db.display_from_table_detail()
        print(rec)

    # }}}
