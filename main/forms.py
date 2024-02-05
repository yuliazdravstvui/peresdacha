from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Product, User


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'photo')


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
