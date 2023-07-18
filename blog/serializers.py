from django.contrib.auth.models import User, Group
from rest_framework import serializers

from blog.models import Post, CustomUser, Images, TechStack


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url',  'email', 'profile_image', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'



class TechStackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TechStack
        fields = '__all__'

class PostSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='post-detail', lookup_field='slug')
    technology = serializers.StringRelatedField(many=True)



    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'image', 'slug', 'technology', 'url']
