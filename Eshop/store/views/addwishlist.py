from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.wishlist import Wishlist
from django.views import View
from store.forms import AddWishlistform
from vq import *

from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
def get(request ):
        form=AddWishlistform()
        if request.method=="POST":
            form = AddWishlistform(request.POST)

            if form.is_valid():
                wf=form.save(commit=False)
                t=get_product_info(form.cleaned_data['product_url'])
                wf.product_name=t[0]
                wf.current_price=t[1]
                customer = request.session.get('customer')
                wf.customer_id=customer
                wf.save()
                return render(request , 'wishlist.html',{'form':form})
            else:
                print("Error is in valid")

        return render(request , 'add_wishlist.html',{'form':form}  )#, {'orders' : orders})

"""def new_item_form(request):
        form=AddWishlistform()
        if request.method=="POST":
            form = AddWishlistform(request.POST)

            if form.is_valid():
                form.save(commit=True)
                return index(request)
            else:
                print("Error is in valid")
        return render(request,'addwishlist.html',{'form':form})
"""
