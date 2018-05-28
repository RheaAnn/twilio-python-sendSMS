from twilio.rest import Client
import random


account_sid = 'AC9cf4cf923496a3e26699cba3dd0a6abb' # Found on Twilio Console Dashboard
auth_token = '769dfb0d2ba8dc28a5fedf68b7406443' # Found on Twilio Console Dashboard

myPhone = '+639420082944' # Phone number you used to verify your Twilio account
TwilioNumber = '+19122448584' # Phone number given to you by Twilio

client = Client('AC9cf4cf923496a3e26699cba3dd0a6abb', '769dfb0d2ba8dc28a5fedf68b7406443')


n = random.randint(5,10)
print("n", n)
a = random.randint(1,10)
print("a", a)
b = random.randint(1,20)
print ("b", b)

def sendSMS(bplevel):
    if(bplevel==1):
        message=client.messages.create(to=myPhone, from_=TwilioNumber, body='status not okay')
    elif(bplevel==2):
        message= client.messages.create(to=myPhone, from_=TwilioNumber, body='status critical')
        
def trigger(n ,a ,b , myPhone, TwilioNumber):
    
    print("inside triggr")      
    if(n==5):
        print("n=5")
        print("okay")
    elif(6<=n<=8):
        print("n = 6 to 8")
        print("borderline")
        bplevel = 1
        print("message.body", message.body)
    elif(9<=n<=10):
        print("9-10")
        print("critical")
        bplevel = 2
        print("message.body", message.body)
    return bplevel

    #return stat





