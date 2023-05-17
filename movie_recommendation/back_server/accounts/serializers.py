from rest_framework import serializers
from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta : 
        model = User
        fields = ('username','email','id')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'like_movies', 'password', 'email', 'followings', 'reviews', 'followers',)
        read_only_fields = ('followings', 'reviews', 'like_movies', 'followers',)