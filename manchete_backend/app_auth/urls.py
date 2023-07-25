from django.urls import include, path

from knox import views as knox_views
from rest_framework import routers

from app_auth.views.LoginView import LoginView
from app_auth.views.ProfileViewSet import ProfileViewSet

router = routers.SimpleRouter()
router.register('profiles', ProfileViewSet, basename='profiles')

urlpatterns = [
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('', include(router.urls))
]
