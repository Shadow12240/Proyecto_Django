from django.db import models
from django.core.exceptions import ValidationError

def validate_positive(value):
    if value <= 0:
        raise ValidationError('El valor debe ser positivo.')

def validate_no_special_chars(value):
    import re
    if re.search(r'[^a-zA-Z0-9 ]', value):
        raise ValidationError('El campo no debe contener caracteres especiales.')

class Category(models.Model):
    name = models.CharField(max_length=100, validators=[validate_no_special_chars])
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[validate_positive])
    stock = models.IntegerField(validators=[validate_positive])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Customer(models.Model):
    name = models.CharField(max_length=100, validators=[validate_no_special_chars])
    email = models.EmailField(unique=True)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[validate_positive])
    date_ordered = models.DateTimeField(auto_now_add=True)