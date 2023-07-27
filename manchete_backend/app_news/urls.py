from django.urls import include, path

from rest_framework import routers

from app_news.views import NewsViewSet, SubmissionListView, SubmissionUpdateView

router = routers.SimpleRouter()
router.register('news', NewsViewSet, basename='news')

urlpatterns = [
    path('news/submissions/', SubmissionListView.as_view(), name='submissions'),
    path('news/publish/<str:pk>/', SubmissionUpdateView.as_view(), name='publish'),
    path('', include(router.urls))
]
