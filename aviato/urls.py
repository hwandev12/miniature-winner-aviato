from django.urls import path
from .views import HomeView, BlogPageView

app_name = 'aviato'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog-info/', BlogPageView.as_view(), name='blog'),
]
