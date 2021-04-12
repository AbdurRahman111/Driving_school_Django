from django.forms import ModelForm
from .models import customer_more_information
from django.contrib.auth.models import User

class change_profile(ModelForm):
    class Meta:
        model = customer_more_information
        fields = ['Phone_number', 'Postcode', 'Address']

class change_user_profile(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
