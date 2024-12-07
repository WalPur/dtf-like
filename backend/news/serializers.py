from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from news.models import Article


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class ArticleSerializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Article
        fields = "__all__"
