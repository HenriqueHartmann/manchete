from django.urls import include, path

from rest_framework import routers

from app_news.views import NewsViewSet

router = routers.SimpleRouter()
router.register('news', NewsViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls))
]
