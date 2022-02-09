from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.deletion import CASCADE


# Create your models here.




class Customer(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

class Activity(models.Model):

    def __str__(self):
        return self.phone_number +':' + self.stage
    phone_number = models.CharField(max_length=30)
    message = models.CharField(max_length=30)
    stage  = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)      




class Company(models.Model):
    
    def __str__(self):
        return self.name 
    adress = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)


    


class Product(models.Model):
    
    def __str__(self):
        return self.name 
    company  = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    description = models.CharField(max_length=300)

class Shop(models.Model):
    
    def __str__(self):
        return self.name
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,default=1)
    adress = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100,default="regular")
    position = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)

class Stage(models.Model):
    MAIN_STAGES = (('M', 'Menu'),('S', 'Search'),('ST', 'Stage'),)
    MENU_STAGES = (('R', 'Register'),('P', 'Add Product'),('S', 'Subscribe'),('RP', 'Report'),('F', 'Feedback'))
    REGISTER_STAGES = (('N', 'Name'),('L', 'Location Details'),('V', 'Verify'),('RP', 'Report'))
    phone_number = models.CharField(max_length=30)
    main_stage = models.CharField(max_length=2, choices=MAIN_STAGES)
    menu_stage = models.CharField(max_length=2, choices=MAIN_STAGES)

    
    
class Transaction(models.Model):
    phoneNumber = models.CharField(max_length=30)
    message = models.CharField(max_length=30)
    amount  = models.CharField(max_length=30)
    status  = models.CharField(max_length=30)
    reference  = models.CharField(max_length=30)
    type  = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

class OrderTemp(models.Model):
    
    def __str__(self):
        return self.name 
    name = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=300)
    done = models.BooleanField(default=False)

class LandLord(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=1000,default='')
    phone_number = models.CharField(max_length=16)
    id_number = models.CharField(null=True)
    id_picture = models.CharField(max_length=5)
    status = models.CharField(max_length=5)
    service = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    males = models.CharField(max_length=100)
    females = models.CharField(max_length=100)
    location = models.CharField(max_length=20,null=True)
    capacity = models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

 
class Order(models.Model):
    delivery_stages = (('W', 'Waiting Delivery'),('D', 'Delivered'),('C', 'Collected'))

    delivery_status = models.CharField(max_length=2, choices=delivery_stages)
    shop = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=16)
    transaction_number = models.IntegerField()
    amount_paid = models.CharField(max_length=5)
    status = models.CharField(max_length=5)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
 


class FindTaxi(models.Model):
    phone_number = models.CharField(max_length=30)
    current_location = models.CharField(max_length=30)
    destination  = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Member(models.Model):
    language_choices =(
    ("English", "English"),
    ("Zulu", "Zulu"),
    ("Xhosa", "Xhosa"),
    ("Afrikaans", "Afrikaans"),
    ("Venda", "Venda"),
    ("Sotho", "Sotho"),
    ("Tswana", "Tswana"),
    ("Tsonga", "Tsonga"),
)
    full_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=16)
    languages = forms.MultipleChoiceField(choices = language_choices) 
    id_picture = models.CharField(max_length=200)
    member_type = models.CharField(max_length=200)
    certification = models.CharField(max_length=16)
    activated = models.CharField(max_length=16)
    subrscibed = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   


    def selected_languages_labels(self):
        return [label for value, label in self.fields['languages'].choices if value in self['languages'].value()]

class WhatsAppUser(models.Model):
    address = models.CharField(max_length=100)
    ecocash_number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=16)