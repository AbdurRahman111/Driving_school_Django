from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
import hashlib
from instructor.models import instructor_information
# Create your models here.


# for sending activation link generation
class EmailConfirmed(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    activation_key=models.CharField(max_length=500)
    email_confirmed=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural='User Email-Confirmed'

@receiver(post_save, sender=User)
def create_user_email_confirmation(sender, instance, created, **kwargs):
    if created:
        dt=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        email_confirmed_instance=EmailConfirmed(user=instance)
        user_encoded=f'{instance.email}-{dt}'.encode()
        activation_key=hashlib.sha224(user_encoded).hexdigest()
        email_confirmed_instance.activation_key=activation_key
        email_confirmed_instance.save()


# lesson Category table
class Categories(models.Model):
    category_name=models.CharField(max_length=500)

    def __str__(self):
        return self.category_name

# lesson table
class products(models.Model):
    product_name = models.CharField(max_length=2000)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    Intructor = models.ForeignKey(instructor_information, on_delete=models.CASCADE)
    product_price = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='uploads/product_image')
    image2 = models.ImageField(upload_to='uploads/product_image', null=True, blank=True, default='')
    image3 = models.ImageField(upload_to='uploads/product_image', null=True, blank=True, default='')
    image4 = models.ImageField(upload_to='uploads/product_image', null=True, blank=True, default='')
    image5 = models.ImageField(upload_to='uploads/product_image', null=True, blank=True, default='')
    description = models.TextField()

    def __str__(self):
        return self.product_name

# for customer more details
class customer_more_information(models.Model):
    Customer = models.ForeignKey(User, on_delete=models.CASCADE)
    Phone_number = models.CharField(max_length=200)
    Postcode = models.CharField(max_length=200, default='')
    Address = models.CharField(max_length=200)
