from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from filter_app.models import Post, UserModel
from filter_app.serializers import PostSerializer, UserSerializer
from rest_framework import filters
from filter_app.filters import PostFilter, UserFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = PostFilter
    # filterset_fields = ['title', "user__name"]
    search_fields = ["title", "user__age"]
    ordering_fields = "__all__"


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = UserFilter
    # filterset_fields = ['name', "age"]
    search_fields = ["name", "age"]
    ordering_fields = "__all__"