from django.db import models

# Create your models here.


class contact_us(models.Model):
    email=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.email