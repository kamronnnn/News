from urllib.request import Request

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import News, Category, Comment
from .serializers import CategorySerializer, NewsSerializer, CommentSerializer


# Create your views here.


class CategoryListView(APIView):
    def get(self, request: Request, pk=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


    def post(self, request: Request, pk=None):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = serializer.save()
        return Response(CategorySerializer(category).data)


    def put(self, request: Request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


# -------------------------------------------------------------------------

class NewsListView(APIView):
    def get(self, request: Request, pk=None):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)


    def post(self, request: Request, pk=None):
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        news = serializer.save()
        return Response(NewsSerializer(news).data)


    def put(self, request: Request, pk):
        news = News.objects.get(pk=pk)
        serializer = NewsSerializer(news, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

# -------------------------------------------------------------------------

class CommentListView(APIView):
    def get(self, request: Request, pk=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


    def post(self, request: Request, pk=None):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        return Response(NewsSerializer(comment).data)


    def put(self, request: Request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
