from twilio.rest import Client
import random


account_sid = 'AC9cf4cf923496a3e26699cba3dd0a6abb' # Found on Twilio Console Dashboard
auth_token = '769dfb0d2ba8dc28a5fedf68b7406443' # Found on Twilio Console Dashboard

client = Client('AC9cf4cf923496a3e26699cba3dd0a6abb', '769dfb0d2ba8dc28a5fedf68b7406443')

def sendSMS(bplevel):
    myPhone = '+639420082944' # Phone number you used to verify your Twilio account
    TwilioNumber = '+19122448584' # Phone number given to you by Twilio

    if (bplevel==1):
        print("pre-hypertensive")
        message=client.messages.create(to=myPhone, from_=TwilioNumber, body='status not okay')
        print("message.body", message.body)
    elif(bplevel==2):
        print("critical")
        message= client.messages.create(to=myPhone, from_=TwilioNumber, body='status critical')
        print("message.body", message.body)
        pass

def values(age, systolic, diastolic):
    print("inside values")
    if (age==5):
        print("you are okay")
    elif(6<=age<=8):
        print("borderline")
        bplevel = 1
    elif(9<=age<=10):
        print("crititcal")
        bplevel = 2
    sendSMS(bplevel);

age = random.randint(5,10)
print("age: ", age)
systolic = random.randint(1,10)
print("systolic: ", systolic)
diastolic = random.randint(1,20)
print ("diastolic", diastolic)
values(age, systolic, diastolic);





