from django.urls import path
from .views import (
    HomeView,
    BlogPageView,
    AboutPageView
)
app_name = 'aviato'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog-info/', BlogPageView.as_view(), name='blog'),
    path('about/', AboutPageView.as_view(), name='about')
]
