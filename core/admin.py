from django.contrib import admin
from .models import Company, Employee, Menu, Order, Cook, Driver

# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Cook)
admin.site.register(Driver) 