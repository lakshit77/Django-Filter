from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from filter_app.models import Post
from filter_app.serializers import PostSerializer
from rest_framework import filters
from django_filters import rest_framework as filter


class PostFilter(filter.FilterSet):
    somethinggg = filter.CharFilter(field_name="title", lookup_expr="iexact")
    age = filter.NumberFilter(field_name="age", lookup_expr="gt")

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ["title"]
    filterset_class = PostFilter
    search_fields = ["title", "content"]
    ordering_fields = "__all__"




    
    