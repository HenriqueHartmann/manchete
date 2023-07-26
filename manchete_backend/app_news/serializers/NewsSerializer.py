from rest_framework import serializers

from app_news.models import News
from app_auth.serializers import ProfileSerializer


class NewsSerializer(serializers.ModelSerializer):
	created_by = ProfileSerializer()
	published_by = ProfileSerializer()
	
	class Meta:
		model = News
		fields = '__all__'


class NewsCreateSerializer(serializers.ModelSerializer):	
	class Meta:
		model = News
		fields = '__all__'

	def create(self, validated_data):
		news = News.objects.create(**validated_data)
		return news
	
class NewsUpdateSerializer(serializers.ModelSerializer):	
	class Meta:
		model = News
		fields = ['title', 'subtitle', 'body',]
