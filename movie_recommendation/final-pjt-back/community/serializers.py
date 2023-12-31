from rest_framework import serializers
from .models import Community, Comment


class CommunityListSerializer(serializers.ModelSerializer):
  userName = serializers.SerializerMethodField()
  userId = serializers.SerializerMethodField()  
  created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
  updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

  
  def get_userName(self,obj):
    return obj.user.username

  def get_userId(self,obj): 
    return obj.user.id

  class Meta:
    model = Community
    fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'user', 'userName', 'userId',)  # 'userId' 필드를 추가
    read_only_fields = ('user',)


class CommunitySerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()

    def get_userName(self, obj):
        return obj.user.username

    class Meta:
        model = Community
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'user', 'userName',)
        read_only_fields = ('user', 'userName',)
        
class CommunityUpdateSerializer(serializers.ModelSerializer):
  userName = serializers.SerializerMethodField()

  def get_userName(self,obj):
    return obj.user.username

  class Meta:
    model = Community
    fields = ('title', 'content','updated_at')


class CommentListSerializer(serializers.ModelSerializer):
  userName = serializers.SerializerMethodField()
  created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
  updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
  
  def get_userName(self,obj):
    return obj.user.username

  class Meta:
    model = Comment
    fields = ('id', 'userName', 'user', 'content', 'created_at', 'updated_at', 'community',)
    read_only_fields = ('user','community',)


class CommentSerializer(serializers.ModelSerializer):
  userName = serializers.SerializerMethodField()
  
  def get_userName(self,obj):
    return obj.user.username

  class Meta:
    model = Comment
    fields = ('id', 'userName', 'user', 'content', 'created_at', 'updated_at', 'community',)
    read_only_fields = ('user','community',)
