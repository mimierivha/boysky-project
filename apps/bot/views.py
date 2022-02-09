
from os import name
from django.core.checks import messages
from django.http import HttpResponse
from twilio.twiml.messaging_response import Message, MessagingResponse
from django.views.decorators.csrf import csrf_exempt
#from .models import 
from paynow import Paynow
import time
from .models import Activity, Customer,Member,FindTaxi,LandLord, OrderTemp, Product, Shop,WhatsAppUser
from twilio.rest import Client
account_sid = "AC90845337f81e8505a6c956fa62db0591"
auth_token = "nsjPS1zWyA41rCTNtJnSE4uSs5F8sF3R"


client = Client(username="AC90845337f81e8505a6c956fa62db0591", password="7c4a07b142f65b575f274d36c926a88c")

@csrf_exempt
def index(request):
    
    if request.method == "POST":
        number = request.POST.get('From')
        user = get_number(request.POST.get('From'))
        message = request.POST.get('Body')
        print("muno")
        print(f'{user} says {message}')
        response = MessagingResponse()
        res = Message()

      # create Activity and Customer

        try:
            activity = Activity.objects.get(phone_number=user)
            customer = Customer.objects.get(phone_number=user)
            print(activity.stage)

        except Activity.DoesNotExist:
            landlord = LandLord(phone_number=user)
            order.save()

            activity = Activity.objects.create(stage='',phone_number=user)
            activity.save()
            
            customer = Customer.objects.create(phone_number=user)
            customer.save()

        try:
            landlord = LandLord.objects.get(phone_number=user)
            print(activity.stage)

        except OrderTable.DoesNotExist:
            landlord = LandLord(phone_number=user)
            landlord.save()  
           


       # in Production  the template comes here      

        if activity.stage == 'user_name' and customer.name == '':
            # return a quote
            customer.name = message
            customer.save()
            landlord.name=customer.name
            activity.stage = "landy_tenant"
            activity.save()
            response.message('Hi '+ customer.name +'\U0001F973'+ 'Please Select Option \n\n1. Register As A LandLord\n2. Looking for A Place To Rent \U0001F917\n\n')
           # response.message('Hi '+ customer.name +'\U0001F973 to myBot Please Select the Following \n\n1. Chicken Inn \n2. KFC \n3. Barcelos \n4. Mambos \n5. Nandos\n')
            return HttpResponse(str(response))

        if customer.name == '':
            # return a quote
            response.message('Hey \U0001F917, My name is Renty, A renting assistant what is your name?') 
            activity.stage = "user_name"
            activity.save()
            return HttpResponse(str(response))     
        
        if ('1' in message ) and activity.stage == 'landy_tenant' :
            
            #response.message('Please Select Shop eg\n\n1. Chicken Inn\n2. Pizza Inn\n3. Cream Inn\n4. KFC\n5. Mambos\n6. Steers\n')
            activity.stage = "id_number"
            activity.save()
            response.message('Please Enter Your Id Number')
            return HttpResponse(str(response)) 

       
                      

        if activity.stage == 'id_number':
            response.message('Please Send A clear Picture of your ID')
            landlord.id_number=message
            activity.stage = "id_picture"
            activity.save()
            return HttpResponse(str(response)) 

        if activity.stage == 'id_picture':
   
            response.message('Please Send Location of your House')
            activity.stage = "location"
            landlord.id_picture=message
            activity.save()
            return HttpResponse(str(response))             

        if activity.stage == 'location':
            response.message('Please Enter The Number of Tenants You Want')
            activity.stage = "capacity"
            landlord.location=message
            activity.save()
            return HttpResponse(str(response))

        if activity.stage == 'capacity':
            response.message('Please Enter Number of Males Occupied \nNB If you only want females enter 0')
            activity.stage = "males"
            landlord.capacity=message
            activity.save()
            return HttpResponse(str(response))      
        if activity.stage == 'males':
            response.message('Please Enter Number of Females Occupied \nNB If you only want males enter 0')
            activity.stage = "females"
            activity.save()
            landlord.males=message
            return HttpResponse(str(response))
        if activity.stage == 'females':
            response.message('Please Enter Your Price')
            activity.stage = "price"
            activity.save()
            landlord.females=message
            return HttpResponse(str(response)) 
        if activity.stage == 'price':
            response.message('Please Enter Service You Provide eg Wifi,Transport')
            activity.stage = "services"
            activity.save()
            landlord.price=message
            return HttpResponse(str(response))   
        if activity.stage == 'services':
            response.message('Thank You For your Response')
            landlord.service=message
            return HttpResponse(str(response))    

        else:
            response.message("Please Enter valid information")    
            return HttpResponse(str(response))
                
            



def send_message(to,body,media):
    message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body=body,
                              to=to,
                              media_url="https://i.pinimg.com/originals/63/4b/a7/634ba7d47141d004984bafce8ce4d3d6.jpg"
                          )

    print(message.sid)

def get_number(phone):
    return phone[9:]