from django_filters import rest_framework as filters
from filter_app.models import Post, UserModel

class UserFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", label="Name is ")
    age = filters.NumberFilter(field_name="age")
    post_title = filters.CharFilter(method="custom_filter", label="Post Title", field_name="title")
    post_content = filters.CharFilter(method="custom_filter", label="Post Content", field_name="content")
    # user = filters.ModelChoiceFilter(queryset = UserModel.objects.all())
    # user_names = filters.ModelMultipleChoiceFilter(field_name='user__id',to_field_name='id',queryset = UserModel.objects.all())

    class Meta:
        model = UserModel
        fields = ['name', 'age']

    def custom_filter(self, queryset, field_name, value):
        res = [
            instance.id
            for instance in queryset
            if instance.user_posts.filter(**{f"{field_name}":f"{value}"})
        ]
        # res = [instance.user_posts.all() for instance in queryset]
        return UserModel.objects.filter(id__in = res)