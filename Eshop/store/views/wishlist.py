from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.wishlist import Wishlist
from django.views import View
from store.models.customer import Customer
from store.middlewares.auth import auth_middleware
from vq import *
class WishlistView(View):


    def get(self,request ):
        customer = request.session.get('customer')
        wishlist = Wishlist.get_wishlist_by_customer(customer)

        return render(request , 'wishlist.html'  , {'wishlist' : wishlist})
