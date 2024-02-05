from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', ViewAbout.as_view(), name='about'),
    path('contacts/', ViewContacts.as_view(), name='contacts'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('service/', ProductList.as_view(), name='service'),
    path('create_service/', CreateProduct.as_view(), name='create_service'),
    path('add_to_basket/<int:product_id>/', AddToBasketView.as_view(), name='add_to_basket'),
    path('register/', RegisterView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)