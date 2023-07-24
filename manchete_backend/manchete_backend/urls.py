from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('manchete-admin/', admin.site.urls),
]
