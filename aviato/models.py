from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class MainHomePageImages(models.Model):
    class Meta:
        verbose_name = 'Home Images'
        verbose_name_plural = 'Home Page Images'

    carousel_img = models.ImageField()
    product_category = models.ImageField()
    trendy_products = models.ImageField()
    instagram = models.ImageField()
