from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Company, Employee, Stage,Member,Activity,LandLord,Shop,Customer,WhatsAppUser,Product

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton

@admin.display(description='Name')
def upper_case_name(obj):
    return ("%s %s" % (obj.stage, obj.phone_number)).upper()


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    fields = ('phone_number', 'message','stage')
    list_display = ('phone_number', 'message','stage',upper_case_name)
    list_display_links = ('phone_number', 'stage')
    list_filter = ('stage','message')
    search_fields = ['stage','phone_number']
    pass

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'
    
# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(LandLord)
class LandLordAdmin(admin.ModelAdmin):
    pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


# Re-register UserAdmin
#admin.site.register(Activity)
#admin.site.register(LandLord)
#admin.site.register(Member)
#admin.site.register(Company)
#admin.site.register(Shop)
#admin.site.register(Customer)
#admin.site.register(WhatsAppUser)
#admin.site.register(Product)