from rest_framework import status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from app_auth.models import Profile
from app_news.models import News
from app_news.serializers import NewsSerializer, NewsCreateSerializer, NewsUpdateSerializer
from manchete_backend.utils.pagination import NewsResultSetPagination
from manchete_backend.utils import validate_user


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    # pagination_class = NewsResultSetPagination

    def get_queryset(self):
        return News.objects.order_by('-created_at', 'id').filter(published=True)
    
    def retrieve(self, request, pk=None):
        news = News.objects.filter(id=pk).first()
        if news == None:
            raise NotFound("Notícia não encontrada.")
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        validate_user.is_user_authenticated(request)
        validate_user.is_user_a_writer_or_super(request)
        profile = Profile.objects.filter(user=request.user.pk).first()
        if profile == None:
            raise NotFound("Perfil não encontrado.")
        request.data['created_by'] = profile.pk
        serializer = NewsCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        validate_user.is_user_authenticated(request)
        validate_user.is_user_an_editor_or_super(request)
        news = News.objects.filter(id=pk).first()
        if news == None:
            raise NotFound("Notícia não encontrada.")
        serializer = NewsUpdateSerializer(news, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def destroy(self, request, pk=None):
        validate_user.is_user_authenticated(request)
        validate_user.is_user_an_editor_or_super(request)
        news = News.objects.all().filter(id=pk).first()
        if news == None:
            raise NotFound("Notícia não encontrada.")
        news.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
