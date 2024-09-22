from django.contrib import admin
from .models import Comment, News, Category

# Register your models here.

admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(News)
