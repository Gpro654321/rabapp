from kivy.uix.screenmanager import Screen

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton


from patient_database import PatientDatabase


class PatientDetailDisplayWindow(MDScreen):
    pass


class PatientDetailLabel(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        patient_db = PatientDatabase()
        rec = patient_db.display_from_table_vacdates()
        print(rec)

        for i in rec:
            
            b = MDLabel(text=str(i[0])+ " - " +str(i[1]),
                       size_hint=(1,float(1/len(rec))),
                       )
            self.add_widget(b)
            print("inside PatientDetailLabel")
            print("added widget")

