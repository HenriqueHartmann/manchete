from django.contrib import admin
from django.urls import include, path

from app_auth import urls as auth_urls

urlpatterns = [
    path('manchete-admin/', admin.site.urls),
    path('api/v1/auth/', include(auth_urls)),
    path('api/v1/', include(auth_urls)),
]
