from django.db import models

# Create your models here.
class User(models.Model):
    # id = models.AutoField(primary_key=True) Django genera de manera automática los id con autoincrement
    username = models.CharField(max_length=150, unique=True)
    age = models.IntegerField()
    password = models.CharField(max_length=128)

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)    

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

class SalesHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

# Si bien en un comienzo parecía buena idea escribir "user_id", buscando sobre los data types, en G4G se dice que es buena práctica asignarle un nombre sin el sufijo id.
# Django agrega el sufijo _id a las FK