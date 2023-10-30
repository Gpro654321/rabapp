from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# for database operations
from patient_database import PatientDatabase


class PatientInputScreen(BoxLayout):
    # {{{ __init__ 

    def __init__(self, **kwargs):
        super(PatientInputScreen, self).__init__(
                                                orientation="vertical",
                                                spacing = 10
                                                )

        # self.cols = 1

        # create labels for the patients details
        self.hamburger_menu_button = Button(text='☰ ')
        self.add_widget(self.hamburger_menu_button)
        self.name_label = Label(text="Name:")
        self.date_of_birth_label = Label(text="Date of birth:")
        self.phone_number_label = Label(text="Phone number:")

        #Create the text inputs
        self.name_text_input = TextInput()
        self.date_of_birth_text_input = TextInput()
        self.phone_number_text_input = TextInput()

        # Button
        self.submit_button = Button(text="Submit")

        # Add the labels and text inputs to the screen
        self.add_widget(self.name_label)
        self.add_widget(self.name_text_input)
        self.add_widget(self.date_of_birth_label)
        self.add_widget(self.date_of_birth_text_input)
        self.add_widget(self.phone_number_label)
        self.add_widget(self.phone_number_text_input)
        self.add_widget(self.submit_button)

        self.submit_button.bind(on_press=self.on_press_button)


    # }}}

    # {{{ on_press_button
    def on_press_button(self, instance):
        
        patient_db = PatientDatabase()

        name = self.name_text_input.text
        dob = self.date_of_birth_text_input.text
        phone = self.phone_number_text_input.text

        patient_db.insert_in_table_detail(name,dob,phone)

        print(self.name_text_input.text)
        print(self.date_of_birth_text_input.text)
        print(self.phone_number_text_input.text)
        
        rec = patient_db.display_from_table_detail()
        print(rec)

    # }}}



