from rest_framework import generics
from django_filters import rest_framework as filters
from filter_app.models import Post, UserModel

class MyMultipleChoiceFilter(filters.ModelMultipleChoiceFilter):
    def get_filter_predicate(self, v):
        return {'id': v.id}

    def filter(self, qs, value):
        if value:
            # qs = qs.annotate_with_custom_field()
            qs = super().filter(qs, value)
        return qs

class PostFilter(filters.FilterSet):
    title = filters.NumberFilter(field_name="title")
    content = filters.NumberFilter(field_name="content")
    user = filters.ModelChoiceFilter(queryset = UserModel.objects.all())
    user_names = filters.ModelMultipleChoiceFilter(field_name='user__id',to_field_name='id',queryset = UserModel.objects.all())
    # user_names = MyMultipleChoiceFilter(to_field_name='id',queryset=UserModel.objects.all(),

    class Meta:
        model = Post
        fields = ['title', 'content', "user"]