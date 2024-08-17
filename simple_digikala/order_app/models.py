from django.db import models
from accounts.models import Costumer, Seller
from product_app.models import Product



class Discount(models.Model):
    active = models.BooleanField(default=True, blank=True, null=True)
    buyer = models.ForeignKey(Costumer, blank=True, null=True)
    code = models.CharField(max_length=10, help_text='code shouldnt be more than 10 characters', blank=True, null=True)
    initiated_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.code

    

class Order(models.Model):
    buyer = models.ForeignKey(Costumer, on_delete = models.CASCADE,blank=True, null=True)
    seller = models.ForeignKey(Seller, on_delete= models.CASCADE,blank=True, null=True)
    transaction_status = models.BooleanField(blank=True, null=True)
    date = models.DateField(help_text='the time when the order was set first', blank=True, null=True)
    discount_code = models.ForeignKey(Discount, on_delete = models.PROTECT, blank=True, null=True)
    bill = models.FloatField(blank=True, null=True)
    code = models.CharField(max_length=10, )

    def __str__(self) -> str:
        return f'{self.buyer}, {self.seller}, {self.code}'
class Order_item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, help_text = 'this item is related to which order', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete= models.CASCADE, help_text='this product', blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    num = models.IntegerField(blank= True, null=True)

    def __str__(self) -> str:
        return f'{self.order}, {self.product}'


    
