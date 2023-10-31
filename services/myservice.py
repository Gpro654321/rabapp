from plyer import sms
import schedule
import time

from jnius import autoclass

PythonService = autoclass('org.kivy.android.PythonService')
PythonService.mService.setAutoRestartService(True)

def test_schedule_send_sms(phone, *largs):
    sms.send(
        recipient = phone,
        message = "Scheduled Message"
    )

def test_service_function():
    print("I am printing......")


schedule.every(15).seconds.do(test_service_function)

while True:
    schedule.run_pending()
    # print("I printing")
    time.sleep(5)
