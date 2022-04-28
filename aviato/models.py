from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Logo(models.Model):
    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logo '

    logo = models.CharField(max_length=100)

    def __str__(self):
        return self.logo


class CarouselImages(models.Model):
    class Meta:
        verbose_name = 'Carousel'
        verbose_name_plural = 'Carousel Images'

    text = models.CharField(max_length=60)
    carousel_img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.text
