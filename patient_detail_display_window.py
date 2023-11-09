from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.button import MDRectangleFlatButton


from patient_database import PatientDatabase


class PatientDetailDisplayWindow(MDScreen):
    def on_enter(self):

        patient_db = PatientDatabase()
        rec = patient_db.display_from_table_vacdates()
        print(rec)

        try:
            # clear all widget before adding anything,
            # because if not cleared every time we move back and forth, 
            # widgets keep getting added
            self.ids["box_layout_2"].clear_widgets()
            print("cleared widgets from box_layout_2")
        except:
            pass

        for i in rec:
            
            b = MDLabel(text=str(i[0])+ " - " +str(i[1]),size_hint_y=None, height=40)
            # need to modify this code
            self.ids["box_layout_2"].add_widget(b)
            print("inside PatientDetailLabel")
            print("added widget")

    pass

        

class PatientDetailLabel(MDBoxLayout):
    pass




