from django.contrib import admin
from .models import Order, cancel_order_for_money_back
# Register your models here.


admin.site.register(Order)
admin.site.register(cancel_order_for_money_back)