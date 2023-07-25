from django.contrib.auth.models import User

from rest_framework import serializers

from app_auth.models.Profile import Profile


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'email', 'is_superuser']


class ProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	
	class Meta:
		model = Profile
		fields = '__all__'


class ProfileCreateSerializer(serializers.ModelSerializer):	
	class Meta:
		model = Profile
		fields = '__all__'

	def create(self, validated_data):
		profile = Profile.objects.create(**validated_data)
		return profile