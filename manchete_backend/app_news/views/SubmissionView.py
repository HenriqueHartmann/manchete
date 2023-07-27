from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from app_auth.models import Profile
from app_news.models import News
from app_news.serializers import NewsSerializer
from manchete_backend.utils import validate_user
from manchete_backend.utils.pagination import NewsResultSetPagination


class SubmissionListView(generics.ListAPIView):
    serializer_class = NewsSerializer
    # pagination_class = NewsResultSetPagination

    def get_queryset(self):
        validate_user.is_user_authenticated(self.request)
        validate_user.is_user_an_editor_or_super(self.request)
        return News.objects.order_by('-created_at', 'id').filter(published=False)


class SubmissionUpdateView(generics.UpdateAPIView):
    def update(self, request, *args, **kwargs):
        validate_user.is_user_authenticated(request)
        validate_user.is_user_an_editor_or_super(request)
        news = News.objects.filter(id=kwargs.get('pk')).first()
        if news == None:
            raise NotFound("Notícia não encontrada.")
        if news.published == False:
            profile = Profile.objects.filter(user=request.user.pk).first()
            if profile == None:
                raise NotFound("Perfil não encontrado.")
            news.published = True
            news.published_by = profile
            news.save()
            return Response({}, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Notícia já foi publicada.'}, status=status.HTTP_400_BAD_REQUEST)
