from django.db import models

class Client(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    cadet = models.BooleanField(default=False)
    faculty = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.firstName, self.lastName)

class Order(models.Model):
    orderDate = models.DateField()
    orderTime = models.TimeField()
    paid = models.BooleanField(default=False)
    orderType = models.CharField(max_length=30)
    quantity = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return self.client

class Item(models.Model):
    stockQuantity = models.IntegerField()
    foodName = models.CharField(max_length=30)
    price = models.IntegerField()
    expirationDate = models.DateField()
    calories = models.IntegerField()
    sodium = models.IntegerField()
    sugar = models.IntegerField()
    fat = models.IntegerField()
    def __str__(self):
        return "%s %s" % ( self.stockQuantity, self.price)
        
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)



