from django.contrib import admin
from .models import (
    CarouselImages,
    Logo,
    UserProfile,
    Agent,
    User
)

admin.site.register(User)
admin.site.register(CarouselImages)
admin.site.register(Logo)
admin.site.register(UserProfile)
admin.site.register(Agent)
