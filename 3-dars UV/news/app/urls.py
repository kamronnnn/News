from django.urls import path
from .views import CategoryListView, NewsListView, CommentListView


urlpatterns = [
    path('api/v1/category/', CategoryListView.as_view()),
    path('api/v1/category/<int:pk>/', CategoryListView.as_view()),

    path('api/v1/news/', NewsListView.as_view()),
    path('api/v1/news/<int:pk>/', NewsListView.as_view()),

    path('api/v1/comment/', CommentListView.as_view()),
    path('api/v1/comment/<int:pk>', CommentListView.as_view()),
]
