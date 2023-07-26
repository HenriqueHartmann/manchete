from django.contrib.auth.models import User

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, NotFound, ValidationError
from rest_framework.response import Response

from app_auth.models import Profile
from app_auth.serializers import ProfileSerializer, ProfileCreatorSerializer, ProfileCreatePartialSerializer, ProfileCreatorWithRoleSerializer, UserSerializer, UserCreatorSerializer, UserCreatorWithGroupSerializer


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
        if not request.user.is_authenticated:
            raise PermissionDenied("Você não tem permissão.")

        serializer = ProfileCreatorSerializer(data=request.data)

        if serializer.is_valid():
            user_serializer = UserCreatorSerializer(
                data=serializer.validated_data['user'])

            if user_serializer.is_valid():
                user = User.objects.all().filter(
                    email=user_serializer.validated_data['email'])
                if user:
                    raise ValidationError({'detail': 'Usuário já existe.'})
                serializer.save()
                return Response({}, status=status.HTTP_201_CREATED)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def create_partial(self, request, pk=None):
        if not request.user.is_authenticated or not request.user.is_superuser:
            raise PermissionDenied("Você não tem permissão.")

        profile = Profile.objects.filter(user=pk).first()
        if profile:
            raise ValidationError({'detail': 'Perfil já existe.'})

        request.data['user'] = pk
        serializer = ProfileCreatePartialSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def create_with_role(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied("Você não tem permissão.")

        serializer = ProfileCreatorWithRoleSerializer(data=request.data)

        if serializer.is_valid():
            user_serializer = UserCreatorWithGroupSerializer(
                data=serializer.validated_data['user'])

            if user_serializer.is_valid():
                user = User.objects.all().filter(
                    email=user_serializer.validated_data['email'])
                if user:
                    raise ValidationError({'detail': 'Usuário já existe.'})
                serializer.save()
                return Response({}, status=status.HTTP_201_CREATED)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
