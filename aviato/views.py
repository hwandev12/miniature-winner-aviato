from .models import CarouselImages
from django.views.generic import (
    TemplateView,
    ListView
)


class HomeView(ListView):
    template_name = 'pages/home.html'
    queryset = CarouselImages.objects.all()
    context_object_name = 'images'


class BlogPageView(TemplateView):
    template_name = 'pages/blog_page.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class DashboardPageView(TemplateView):
    template_name = 'pages/dashboard.html'


class OrdersPageView(TemplateView):
    template_name = 'pages/orders.html'
