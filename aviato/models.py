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

    paragraph = models.CharField(max_length=60)
    menu = models.TextField(max_length=200)
    button = models.CharField(max_length=60)
    carousel_img = models.ImageField(blank=True, null=True)
    organiser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey(
        "Agent", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.paragraph


class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Category'

    product_category_box_head = models.CharField(max_length=150)
    product_category_box_text = models.CharField(max_length=200)
    product_category_box_carousel = models.ImageField(blank=False)
    organiser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey(
        'Agent', null=True, blank=True, on_delete=models.SET_NULL)
    category_model = models.ForeignKey(
        'ProductSingleCategory', blank=False, related_name='category', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.product_category_box_head

# trendy products


class TrendyProducts(models.Model):
    class Meta:
        verbose_name = 'Trendy Products'
        verbose_name_plural = 'Trendy Products'

    trendy_products_type = models.CharField(max_length=200, blank=False)
    trendy_products_cost = models.IntegerField(default=30, blank=False)
    trendy_products_sale = models.CharField(max_length=80, blank=True)
    trendy_products_image = models.ImageField(blank=False)
    organiser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    trendy_category = models.ForeignKey(
        'TrendyProductsCategory', null=True, blank=False, on_delete=models.SET_NULL)

    def __str__(self):
        return self.trendy_products_type

# subscribe newspaper model


class SubscribeNewpaperModel(models.Model):
    class Meta:
        verbose_name = 'Subscribe Newspaper'
        verbose_name_plural = 'Subscribe Newspaper'

    subscribe_newspaper_header = models.CharField(max_length=200, blank=True)
    subscribe_newspaper_text = models.TextField(max_length=350, blank=True)

    def __str__(self):
        return self.subscribe_newspaper_header

# view instagram model


class InstagramSocialModel(models.Model):
    class Meta:
        verbose_name = 'Instagram View'
        verbose_name_plural = 'Instagram View'

    instagram_view_image = models.ImageField(blank=True)
    instagram_category = models.ForeignKey(
        'InstagramCategoryModel', blank=False, null=True, on_delete=models.SET_NULL)
    organiser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.instagram_category)
    
    
# create footer section
class FooterModel(models.Model):
    class Meta:
        verbose_name = 'Footer'
        verbose_name = 'Footer'
        
    footer_copyright = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.footer_copyright)

# create instagram category model
class InstagramCategoryModel(models.Model):
    class Meta:
        verbose_name = 'Instagram Category'
        verbose_name = 'Instagram Category'
        
    instagram_category_name = models.CharField(max_length=200)
    organiser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.instagram_category_name

class TrendyProductsCategory(models.Model):
    class Meta:
        verbose_name = 'Trendy Category'
        verbose_name_plural = 'Trendy Category'

    trendy_products_category = models.CharField(max_length=100)
    organiser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.trendy_products_category


class ProductSingleCategory(models.Model):
    class Meta:
        verbose_name = 'Product Category Model'
        verbose_name_plural = 'Product Category Model'

    product_category_model = models.CharField(max_length=150)
    organiser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_category_model


# agent class here
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organiser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

# That is actually for userprofile when created a user in the website or signed up


def post_save_model(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_save_model, sender=User)
