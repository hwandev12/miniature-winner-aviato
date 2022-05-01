from django.contrib import admin
from .models import (
    CarouselImages,
    Header,
    UserProfile,
    Agent,
    ProductCategory,
    ProductSingleCategory,
    TrendyProducts,
    TrendyProductsCategory,
    SubscribeNewpaperModel,
    InstagramSocialModel,
    User
)

# import user
admin.site.register(User)
# import base header and carousel
admin.site.register(CarouselImages)
admin.site.register(Header)
# import product category
admin.site.register(ProductCategory)
admin.site.register(ProductSingleCategory)
# import trendy products
admin.site.register(TrendyProducts)
admin.site.register(TrendyProductsCategory)
# import subscribe newpaper
admin.site.register(SubscribeNewpaperModel)
# import social instagarm model
admin.site.register(InstagramSocialModel)


# import basic agent and userprofiles
admin.site.register(UserProfile)
admin.site.register(Agent)
