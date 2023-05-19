from rest_framework import serializers
from .models import Movie, Genre, Actor, MovieLike, MovieReview

class GenrenameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name',)

class ActornameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name','profile_path')

class MovieSerializer(serializers.ModelSerializer):
    genres = GenrenameSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users', 'actors')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = ('id','user','movie','content','rate','like','created_at','updated_at')