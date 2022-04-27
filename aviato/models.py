from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class MainHomePageImages(models.Model):
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home Page Images'

    text = models.CharField(max_length=60)
    carousel_img = models.ImageField()
    product_category = models.ImageField()
    trendy_products = models.ImageField()
    instagram = models.ImageField()

    def __str__(self):
        return self.text
