from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from .models import Blog, Author, Category
from .serializers import BlogSerializer, AuthorSerializer, CategorySerializer

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.select_related("user").all()
    serializer_class = AuthorSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
