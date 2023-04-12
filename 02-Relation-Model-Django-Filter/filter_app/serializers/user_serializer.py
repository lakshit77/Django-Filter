from rest_framework import serializers
from filter_app.models import UserModel
from filter_app.serializers import PostSerializer

class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many = True, required = False, source = "user_posts")
    # posts = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = '__all__'
        depth = 1

    def get_posts(self, obj):
        return [wgm.id for wgm in obj.user_posts.all()]