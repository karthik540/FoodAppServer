from django.contrib import admin

# Register your models here.
from .models import Food, Order, Table

admin.site.register(Food)
admin.site.register(Table)
admin.site.register(Order)