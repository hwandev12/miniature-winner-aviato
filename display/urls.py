from django.urls import path
from .views import display

app_name = 'display'

urlpatterns = [
    path('', display, name='display'),
]