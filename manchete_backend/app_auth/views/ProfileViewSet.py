from django.contrib.auth.models import User

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied, NotFound, ValidationError
from rest_framework.response import Response

from app_auth.models import Profile
from app_auth.serializers import ProfileSerializer, ProfileCreatorSerializer, ProfileCreatePartialSerializer, ProfileCreatorWithRoleSerializer, UserCreatorSerializer, UserCreatorWithGroupSerializer
from manchete_backend.utils.pagination import ProfileResultSetPagination
from manchete_backend.utils import validate_user


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    pagination_class = ProfileResultSetPagination

    def get_queryset(self):
        validate_user.is_user_super(self.request)
        return Profile.objects.order_by('-created_at', 'id')

    def retrieve(self, request, pk=None):
        validate_user.is_user_authenticated(request)
        profile = Profile.objects.filter(id=pk).first()
        if profile == None:
            raise NotFound("Perfil não encontrado.")
        if profile.user != request.user:
            raise PermissionDenied("Você não tem permissão.")
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        validate_user.is_user_authenticated(request)
        serializer = ProfileCreatorSerializer(data=request.data)
        if serializer.is_valid():
            user_serializer = UserCreatorSerializer(
                data=serializer.validated_data['user'])
            if user_serializer.is_valid():
                user = User.objects.filter(
                    email=user_serializer.validated_data['email']).first()
                if user:
                    raise ValidationError({'detail': 'Usuário já existe.'})
                serializer.save()
                return Response({}, status=status.HTTP_201_CREATED)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def create_partial(self, request, pk=None):
        validate_user.is_user_authenticated(request)
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
        validate_user.is_user_authenticated()
        serializer = ProfileCreatorWithRoleSerializer(data=request.data)
        if serializer.is_valid():
            user_serializer = UserCreatorWithGroupSerializer(
                data=serializer.validated_data['user'])
            if user_serializer.is_valid():
                user = User.objects.filter(
                    email=user_serializer.validated_data['email'])
                if user:
                    raise ValidationError({'detail': 'Usuário já existe.'})
                serializer.save()
                return Response({}, status=status.HTTP_201_CREATED)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
