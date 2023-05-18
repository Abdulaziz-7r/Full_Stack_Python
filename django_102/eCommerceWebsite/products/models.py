from django.db import models

class Seller(models.Model):
    name = models.CharField(help_text='seller name', max_length=50)
    phone = models.CharField(help_text='seller contact number', max_length=20)
    email = models.EmailField(help_text='seller contact email', max_length=254)
    profile = models.TextField(blank=True, help_text="seller's profile")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(help_text="product's name", max_length=50)
    description = models.TextField(blank=True, help_text="product's description")
    price = models.DecimalField(help_text="product's price", max_digits=5, decimal_places=2)
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
