from django.contrib.auth.models import Group, User

from rest_framework import serializers

from app_auth.models import Profile


class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'groups', 'is_superuser']


class UserCreatorSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, max_length=150)
    last_name = serializers.CharField(required=True, max_length=150)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        required=True, style={'input_type': 'password'})


class UserCreatorWithGroupSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, max_length=150)
    last_name = serializers.CharField(required=True, max_length=150)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        required=True, style={'input_type': 'password'})
    groups = serializers.ListField(
        child=serializers.CharField(max_length=20)
    )


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileCreatorSerializer(serializers.ModelSerializer):
    user = UserCreatorSerializer()

    class Meta:
        model = Profile
        fields = "__all__"

    def create(self, validated_data):
        formatted_data = validated_data['user']
        validated_data.pop('user')
        formatted_data['username'] = formatted_data['email']
        user = User.objects.create(**formatted_data)
        profile = Profile.objects.create(**validated_data, user=user)
        return profile


class ProfileCreatePartialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        profile = Profile.objects.create(**validated_data)
        return profile


class ProfileCreatorWithRoleSerializer(serializers.ModelSerializer):
    user = UserCreatorWithGroupSerializer()

    class Meta:
        model = Profile
        fields = "__all__"

    def create(self, validated_data):
        formatted_data = validated_data['user']
        validated_data.pop('user')
        formatted_data['username'] = formatted_data['email']
        my_groups = formatted_data['groups']
        formatted_data.pop('groups')
        user = User.objects.create(**formatted_data)
        groups = Group.objects.all()
        for g in groups:
            if g.name in my_groups:
                user.groups.add(g)
        user.save()
        profile = Profile.objects.create(**validated_data, user=user)
        return profile
