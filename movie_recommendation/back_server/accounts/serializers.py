from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'is_staff', 'is_active', 'first_name', 'last_name', 'date_joined', 'last_login', 'followings', 'followers','like_movies')
        read_only_fields = ('password', 'is_staff', 'is_active', 'date_joined', 'last_login', 'followings', 'followers','like_movies')