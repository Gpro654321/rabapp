# main.py
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


from patient_input_screen import PatientInputScreen
# from test_multiscreen import WindowManager
from window_manager import WindowManager
from patient_detail_input_window import PatientDetailInputWindow
from patient_detail_display_window import PatientDetailDisplayWindow

# for sliding up the screen above the mobile keyboard
Window.keyboard_anim_args = {'d':.2,'t':'in_out_expo'}
Window.softinput_mode = 'below_target'


kv = Builder.load_file('./windowmanager.kv')


class RabiesSmsApp(App):
    def build(self):
        return kv


'''

class RabiesSmsApp(App):
    def build(self):
        return PatientInputScreen() 


'''

if __name__ == "__main__":
    app = RabiesSmsApp()
    app.run()
