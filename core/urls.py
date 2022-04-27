from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LoginView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aviato.urls')),
    path('login/', LoginView.as_view(), name='login')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
