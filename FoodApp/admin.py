from django.contrib import admin

from .models import Food, Order, Table, Restaurant

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Table)
admin.site.register(Order)