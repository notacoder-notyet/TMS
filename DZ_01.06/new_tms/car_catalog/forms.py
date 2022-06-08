from django import forms

from .models import CarBaseModel, CarBrand, CarModel, Engine

class CarBaseModel(models.Model):
    CHOICES = (
        ('US', 'United States'),
        ('FR', 'France'),
        ('CN', 'China'),
        ('RU', 'Russia'),
        ('SW', 'Sweden'),
    )
    name = models.CharField(max_length=50)
    made_in = models.CharField(max_length=50, choices=CHOICES)
    model_years = models.DateField()

class CarBrandForm(forms.Form):
    name = forms.CharField(max_length=50)
    made_in = forms.ChoiceField(choices=CHOICES)
    model_years = forms.CharField()
    name = forms.CharField(max_length=50, unique=True)
    founded = forms.CharField(auto_now=False, auto_now_add=False)
    headquaters = forms.CharField(max_length=50)
    logo = forms.FileField(required=False)



class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)