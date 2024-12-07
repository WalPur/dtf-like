from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    name = models.TextField("Название статьи")
    author = models.ForeignKey(User, models.CASCADE)
    preview = models.ImageField("Превью")
    content = models.TextField("Содержимое")
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    date_edited = models.DateTimeField("Дата редактирования", auto_now=True)
    views_count = models.IntegerField("Кол-во просмотров", default=0)

    def __str__(self):
        return f"{self.author} - {self.name}"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
