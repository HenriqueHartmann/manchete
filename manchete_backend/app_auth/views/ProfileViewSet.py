from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, NotFound, ValidationError
from rest_framework.response import Response

from app_auth.models import Profile
from app_auth.serializers import ProfileSerializer, ProfileCreateSerializer


class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return Profile.objects.all().order_by('-created_at', 'id')


    def list(self, request):
        if not request.user.is_authenticated or not request.user.is_superuser:
            raise PermissionDenied("Você não tem permissão.")

        serializer = ProfileSerializer(self.get_queryset(), many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def retrieve(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("Você não tem permissão.")

        profile = self.get_queryset().filter(id=kwargs.get('pk')).first()
        
        if profile == None:
            raise NotFound("Perfil não encontrado.")

        if profile.user != request.user:
            raise PermissionDenied("Você não tem permissão.")

        serializer = ProfileSerializer(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        if not request.user.is_authenticated or not request.user.is_superuser:
            raise PermissionDenied("Você não tem permissão.")
        
        serializer = ProfileCreateSerializer(data=request.data)

        if serializer.is_valid():
            profile = Profile.objects.filter(user=serializer.validated_data['user'])
            if profile:
                raise ValidationError({'detail': 'Perfil já existe.'})
            serializer.save()
            return Response({}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
