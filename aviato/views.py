from .models import *
from django.views.generic import (
    TemplateView,
    ListView
)


class HomeView(ListView):
    template_name = 'pages/home.html'


    # it is for multiple context objects
    def get_queryset(self):
        return Header.objects.all()

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(HomeView, self).get_context_data(**kwargs)
        # here we can add so many context using that way
        context['images'] = CarouselImages.objects.all()
        context['logos'] = Header.objects.all()
        context['products'] = ProductCategory.objects.all()
        context['categories'] = ProductSingleCategory.objects.all()
        context['trendy_products'] = TrendyProducts.objects.all()
        context['trendy_products_categories'] = TrendyProductsCategory.objects.all()
        context['subscribe_newspapers'] = SubscribeNewpaperModel.objects.all()
        context['instagram_social'] = InstagramSocialModel.objects.all()
        context['instagram_model_category'] = InstagramCategoryModel.objects.all()
        context['footer_sections'] = FooterModel.objects.all()
        return context


class BlogPageView(TemplateView):
    template_name = 'pages/blog_page.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class DashboardPageView(TemplateView):
    template_name = 'pages/dashboard.html'


class OrdersPageView(TemplateView):
    template_name = 'pages/orders.html'
    
class ShopPageView(ListView):
    template_name = 'pages/shop.html'
    
    def get_queryset(self):
        return TrendyProducts.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ShopPageView, self).get_context_data(**kwargs)
        context['trendy_products'] = TrendyProducts.objects.all()
        return context