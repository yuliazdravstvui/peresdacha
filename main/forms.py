from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Product, AdvUser


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'photo')


class RegistrationForm(UserCreationForm):
    class Meta:
        model = AdvUser
        fields = ['username', 'email', 'password1', 'password2']