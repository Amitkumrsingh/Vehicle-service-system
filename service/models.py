from django.db import models

class Component(models.Model):
    name = models.CharField(max_length=100)
    repair_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class Vehicle(models.Model):
    model = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20, unique=True)
    owner = models.CharField(max_length=100)

class Issue(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    description = models.TextField()
    component_needed = models.ForeignKey(Component, null=True, blank=True, on_delete=models.SET_NULL)
    is_repair = models.BooleanField(default=False)

class Transaction(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

