from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    is_organiser = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)


class Header(models.Model):
    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Header'
        
    phone = models.IntegerField(default=998)
    logo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.logo


class CarouselImages(models.Model):
    class Meta:
        verbose_name = 'Carousel'
        verbose_name_plural = 'Carousel Images'

    text = models.CharField(max_length=60)
    carousel_img = models.ImageField(blank=True, null=True)
    organiser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey(
        "Agent", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


# agent class here
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organiser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


def post_save_model(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_save_model, sender=User)
