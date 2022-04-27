from django.urls import path
from .views import (
    HomeView,
    BlogPageView,
    AboutPageView,
    DashboardPageView
)
app_name = 'aviato'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog-info/', BlogPageView.as_view(), name='blog'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard')
]
