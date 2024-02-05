from django.contrib.auth.models import AbstractUser
from django.db import models

class AdvUser(AbstractUser):
    basket = models.ManyToManyField('Product', blank=True, related_name='basket')

    class Meta:
        pass

class Product(models.Model):
    description = models.TextField(verbose_name='Описание товара')
    photo = models.ImageField(upload_to='media/', default=None, verbose_name='Фото товара')




