from rest_framework import status, viewsets
from rest_framework.exceptions import PermissionDenied, NotFound, ValidationError
from rest_framework.response import Response

from app_auth.models import Profile
from app_news.models import News
from app_news.serializers import NewsSerializer, NewsCreateSerializer


class NewsViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return News.objects.all().order_by('-created_at', 'id')

    def list(self, request):
        serializer = NewsSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def retrieve(self, request, *args, **kwargs):
        news = self.get_queryset().filter(id=kwargs.get('pk')).first()
        
        if news == None:
            raise NotFound("Notícia não encontrada.")

        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        if not request.user.is_authenticated: 
            raise PermissionDenied("Você não tem permissão.")
        
        if request.user.groups.filter(name='writer').exists() == False or not request.user.is_superuser:
            raise PermissionDenied("Você não tem permissão.")

        profile = Profile.objects.all().filter(user=request.user.pk).first()

        if profile == None:
            raise NotFound("Perfil não encontrado.")

        request.data['created_by'] = profile.pk
        serializer = NewsCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        if not request.user.is_authenticated: 
            raise PermissionDenied("Você não tem permissão.")
        
        if request.user.groups.filter(name='editor').exists() == False:
            if not request.user.is_superuser:
                raise PermissionDenied("Você não tem permissão.")
        
        news = News.objects.all().filter(id=pk).first()

        if news == None:
            raise NotFound("Notícia não encontrada.")

        news.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)


# Create Permissions
# List Submissions
# Update News
# Update Submission

