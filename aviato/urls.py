from django.urls import path
from .views import (
    HomeView,
    BlogPageView,
    AboutPageView,
    DashboardPageView,
    OrdersPageView,
    ShopPageView
)
app_name = 'aviato'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog-info/', BlogPageView.as_view(), name='blog'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('orders/', OrdersPageView.as_view(), name='order'),
    path('shopping-cards/', ShopPageView.as_view(), name='shop'),
]
