from django.contrib import admin

from .models import Client
from .models import Order
from .models import Item
from .models import OrderItem

# Register your models here.
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(OrderItem)

