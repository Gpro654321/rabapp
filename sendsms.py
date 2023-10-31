from plyer import sms


from patient_database import PatientDatabase

def get_numbers_to_send_sms():

    # instantiate the patient database
    patient_db = PatientDatabase()

    rec2 = patient_db.display_from_table_vacdates_on_a_date('2023-11-03')

    phone = []

    for i in rec2:
        phone.append(i[0])

    return phone

def send_sms(phone):
    sms.send(
        recipient=phone,
        message = "Test Message"
    )
    print("message sent")

def send_remainders():
    phone = get_numbers_to_send_sms()

    for i in phone:
        send_sms(i)

