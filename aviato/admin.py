from django.contrib import admin
from .models import (
    CarouselImages,
    Header,
    UserProfile,
    Agent,
    ProductCategory,
    User
)

# import user
admin.site.register(User)
# import base header and carousel
admin.site.register(CarouselImages)
admin.site.register(Header)
# import product category
admin.site.register(ProductCategory)


# import basic agent and userprofiles
admin.site.register(UserProfile)
admin.site.register(Agent)
