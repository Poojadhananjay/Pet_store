from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer,Address

class UserForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=15)


    class Meta():
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
    # these fileds are available in  url , this form where we giving the input
    #  from modles:  'first_name', 'last_name','email' are taken
 # from usercreation: 'username',    'password1','password2', are taken

class CustomerForm(forms.ModelForm) :
    class Meta:
        model = Customer
        fields = ['phone']


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = [
            'building_name',
            'street',
            'landmark',
            'city',
            'state',
            'zipcode'

        ]        



class SetAddressForm(forms.Form):
    delivery_address = forms.CharField()

