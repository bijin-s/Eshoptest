from testtest1 import *
from .store.models.wishlist import Wishlist
def my_cron_job():
 wl=Wishlist..objects.all()
 for w in wl:
  
  if w.current_price<w.price:
   print(w.product_name)
   send_email(w.product_name)