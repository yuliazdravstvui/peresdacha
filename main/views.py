from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView
from .models import *
from .forms import CreateProductForm, RegistrationForm


def index(request):
    return render(request, 'main/index.html')


class LoginView(LoginView):
    template_name = 'main/login.html'
    success_url = reverse_lazy('main:create_service')


class ViewAbout(TemplateView):
    template_name = 'main/about.html'


class ViewContacts(TemplateView):
    template_name = 'main/contacts.html'


class ProductList(ListView):
    model = Product
    template_name = 'main/service.html'
    context_object_name = 'products'


class CreateProduct(CreateView):
    model = Product
    template_name = 'main/create_product.html'
    form_class = CreateProductForm
    success_url = reverse_lazy('main:service')


class BasketView(TemplateView):
    template_name = 'main/basket.html'


class AddToBasketView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        user = self.request.user

        if product not in user.basket.all():
            user.basket.add(product)
            return redirect('main:service')
        else:
            return HttpResponseBadRequest("The product is already in the cart")


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'main/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:index')
        return render(request, 'main/register.html', {'form': form})
