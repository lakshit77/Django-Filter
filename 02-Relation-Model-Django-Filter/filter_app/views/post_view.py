from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from filter_app.models import Post
from filter_app.serializers import PostSerializer
from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['title', "user__name"]
    search_fields = ["title", "user__age"]
    ordering_fields = "__all__"