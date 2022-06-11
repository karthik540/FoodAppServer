from operator import truediv
from django.db import models

# Create your models here.

class Food(models.Model):
    foodId = models.AutoField(primary_key= True, db_column= 'foodId')
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    isAvailable = models.BooleanField()
    def __str__(self):
        return str(self.foodId) + " | Name = " + self.name

class Table(models.Model):
    tableId = models.AutoField(primary_key= True, db_column= 'tableId')
    isOccupied = models.BooleanField()
    sessionId = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.tableId) + " | Availability = " + str(self.isOccupied)

class Order(models.Model):
    orderId = models.AutoField(primary_key= True, db_column= 'orderId')
    tableId = models.ForeignKey(Table, on_delete=models.CASCADE)
    sessionId = models.IntegerField()
    foodID = models.ForeignKey(Food, on_delete=models.CASCADE)
    foodQuantity = models.IntegerField()