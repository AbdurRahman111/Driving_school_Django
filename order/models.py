from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from instructor.models import instructor_information
from home.models import products
# Create your models here.


# order table for store all order details
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Lesson = models.ForeignKey(products, on_delete=models.CASCADE, blank=True, null=True)
    Instructor = models.ForeignKey(instructor_information, on_delete=models.CASCADE, blank=True, null=True)
    order_id = models.CharField(max_length=1000)
    Lesson_price = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    zip = models.CharField(max_length=1000)
    ordered = models.BooleanField(default=False)
    instructor_cancel_order = models.BooleanField(default=False)
    customer_cancel_order = models.BooleanField(default=False)
    # order_date = models.DateField(default=datetime.now(), blank=True)
    order_date = models.CharField(max_length=1000)

# table for all cancel order in less then 24 hours
class cancel_order_for_money_back(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Cancel_Time = models.DateTimeField(default=datetime.now(), blank=True)