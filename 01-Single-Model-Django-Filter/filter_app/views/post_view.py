from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from filter_app.models import Post
from filter_app.serializers import PostSerializer
from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["title"]
    ordering_fields = "__all__"
    