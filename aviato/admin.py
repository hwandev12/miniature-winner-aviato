from django.contrib import admin
from .models import (
    CarouselImages,
    Logo,
    UserProfile
)

admin.site.register(CarouselImages)
admin.site.register(Logo)
admin.site.register(UserProfile)
