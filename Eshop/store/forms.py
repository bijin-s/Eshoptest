from django import forms
from django.contrib.auth.models import User
from store.models.wishlist import Wishlist
from vq import *
class AddWishlistform(forms.ModelForm):
    #add validations here

    class Meta:
        model= Wishlist
        fields=["product_url","price"]
        
