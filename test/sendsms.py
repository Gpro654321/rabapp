from plyer import sms


from patient_database import PatientDatabase

def get_numbers_to_send_sms():

    # instantiate the patient database
    patient_db = PatientDatabase()

    # this method returns the name and phone of the patient
    rec2 = patient_db.display_from_table_vacdates_on_a_date('2023-11-04')
    
    


    phone = []

    for i in rec2:
        phone.append([i[0],i[1]])

    print(phone)

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
        send_sms(i[1])

