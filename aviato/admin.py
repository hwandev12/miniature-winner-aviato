from django.contrib import admin
from .models import (
    CarouselImages,
    Header,
    UserProfile,
    Agent,
    User
)

admin.site.register(User)
admin.site.register(CarouselImages)
admin.site.register(Header)
admin.site.register(UserProfile)
admin.site.register(Agent)
