from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Kategoriya nomi')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Kategoriya qo\'shilgan vaqt')

    def __str__(self):
        return self.name

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Yangilik nomi')
    description = models.TextField(verbose_name='Tavsifi')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Yangilik qo\'shilgan vaqt')

    def __str__(self):
        return self.name

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=50, verbose_name='Muallif ismi')
    content = models.TextField(verbose_name='Izoh matni')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Izoh qoldirilgan vaqt')

    def __str__(self):
        return self.author_name