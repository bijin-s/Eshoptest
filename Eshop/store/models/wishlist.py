from django.db import models
from vq import *
from .customer import Customer
class Wishlist(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)

    price= models.IntegerField(default=100)
    product_url= models.URLField()
    product_name=models.CharField(max_length=250)
    current_price= models.IntegerField(default=100)


    def addtow(self):
        self.save()
    @staticmethod
    def get_wishlist_by_customer(customer_id):
        return Wishlist.objects.filter(customer=customer_id)
