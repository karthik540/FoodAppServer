from django.db import models

# Create your models here.
class Restaurant(models.Model):
    restaurantId = models.AutoField(primary_key= True, db_column= 'restaurantId')
    name = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

class Food(models.Model):
    foodId = models.AutoField(primary_key= True, db_column= 'foodId')
    restaurantId = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    isAvailable = models.BooleanField()
    imageUrl = models.CharField(max_length=400)
    def __str__(self):
        return str(self.foodId) + " | Name = " + self.name

class Table(models.Model):
    class Meta:
        unique_together = (('restaurantId', 'tableId'),)    
    restaurantId = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    tableId = models.IntegerField()
    isOccupied = models.BooleanField()
    sessionId = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.tableId) + " | Availability = " + str(self.isOccupied)

class Order(models.Model):
    orderId = models.AutoField(primary_key= True, db_column= 'orderId')    
    restaurantId = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    tableId = models.ForeignKey(Table, on_delete=models.CASCADE)
    sessionId = models.IntegerField()
    foodID = models.ForeignKey(Food, on_delete=models.CASCADE)
    foodQuantity = models.IntegerField()