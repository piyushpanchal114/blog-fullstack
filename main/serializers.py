from rest_framework import serializers
from django.conf import settings
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import Blog, Author, Category, SubCategory

    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title"]

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ["id", "title"] 

class UserSerializer(serializers.ModelSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'first_name', 'last_name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "avatar", "user"]
    user = UserSerializer()
    # user = serializers.StringRelatedField()

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "title", "description", "category", "sub_category", "created_at", "author", "cover"]

    category = serializers.StringRelatedField()
    # sub_category = serializers.StringRelatedField()
    # sub_category = serializers.StringRelatedField(many=True)
    # author = serializers.StringRelatedField(many=True)
    author = AuthorSerializer()
