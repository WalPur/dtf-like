from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from news.models import Article
from news.serializers import ArticleSerializer


class ArticleViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Article.objects.all().order_by("-date_created")
    serializer_class = ArticleSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
