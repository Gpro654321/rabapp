# main.py
# from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import platform
# from jnius import autoclass

# if android request permissions
# Watch following video on how to add permissions to your app
# "https://www.youtube.com/watch?v=okpiDnSR4z8"
if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.SEND_SMS,Permission.VIBRATE])


from patient_input_screen import PatientInputScreen
# from test_multiscreen import WindowManager
from window_manager import WindowManager
from patient_detail_input_window import PatientDetailInputWindow
from patient_detail_display_window import PatientDetailDisplayWindow

# for sliding up the screen above the mobile keyboard
Window.keyboard_anim_args = {'d':.2,'t':'in_out_expo'}
Window.softinput_mode = 'below_target'




class RabiesSmsApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        kv = Builder.load_file('./windowmanager.kv')
        return kv

    def on_start(self, **kwargs):
        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.SEND_SMS, Permission.VIBRATE])

            # start service
            self.start_service()
            print("started_service")


    @staticmethod
    def start_service():
        # got it from here "https://www.youtube.com/watch?v=f57ItZCtliM&t=718s"
        service = autoclass('org.rabapp.rabapp.ServiceMyservice')
        mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
        argument = ''
        service.start(mActivity, argument)


if __name__ == "__main__":
    app = RabiesSmsApp()
    app.run()
