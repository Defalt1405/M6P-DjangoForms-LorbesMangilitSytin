from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    def getName(self):
        return self.name
    
    def __str__(self):
        return f'{self.name} - {self.city}, {self.country} created at: {self.created_at}'

class WaterBottle(models.Model):
    SKU = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=100)
    mouth_size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    supplied_by = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    current_quantity = models.IntegerField()

    def __str__(self):
        return f'{self.SKU}: {self.brand}, {self.mouth_size} Mouth, {self.size}, {self.color}, supplied by {self.supplied_by.name}, {self.cost}: {self.current_quantity}'

class Accounts(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password

    def __str__(self):
        return self.username