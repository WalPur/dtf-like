from django.contrib import admin

from news.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["name", "author", "views_count"]
