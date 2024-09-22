from rest_framework import serializers
from .models import Comment, Category, News

# -------------------------------------------------------------------------

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Category(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

# -------------------------------------------------------------------------

class NewsSerializer(serializers.Serializer):
    category_id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return News(**validated_data)

    def update(self, instance, validated_data):
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

# -------------------------------------------------------------------------


class CommentSerializer(serializers.Serializer):
    news = serializers.IntegerField()
    author_name = serializers.CharField(max_length=50)
    content = serializers.CharField()
    crated = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.news_id = validated_data.get('news_id', instance.news_id)
        instance.author_name = validated_data.get('author_name', instance.author_name)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
