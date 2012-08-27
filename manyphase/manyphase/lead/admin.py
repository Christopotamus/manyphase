from django.contrib import admin
from models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('pk','first_name', 'last_name', 'url', 'email')
admin.site.register(Customer, CustomerAdmin)

