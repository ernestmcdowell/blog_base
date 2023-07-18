from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, ImageSerializer, TechStackSerializer

from blog.models import Post, CustomUser, Images, TechStack
from blog.serializers import PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer


class TechStackViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TechStack.objects.all()
    serializer_class = TechStackSerializer
