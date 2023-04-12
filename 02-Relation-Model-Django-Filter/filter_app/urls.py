from django.urls import include, path
from rest_framework import routers
from filter_app.views import PostViewSet, UserViewSet

post_router = routers.DefaultRouter()
post_router.register('posts', PostViewSet, basename="posts")

user_router = routers.DefaultRouter()
user_router.register('users', UserViewSet, basename="users")

urlpatterns = [
    path('', include(post_router.urls)),
    path('', include(user_router.urls)),
]