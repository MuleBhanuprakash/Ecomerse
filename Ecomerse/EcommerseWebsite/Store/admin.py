from django.contrib import admin
#from .models import ShippingAddress,Customer,Product,Order,OrderId
from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderId)
admin.site.register(ShippingAddress)

