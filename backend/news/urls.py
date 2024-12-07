from django.urls import include, path
from rest_framework.routers import DefaultRouter

from news.views import ArticleViewSet

router = DefaultRouter()
router.register("", ArticleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
