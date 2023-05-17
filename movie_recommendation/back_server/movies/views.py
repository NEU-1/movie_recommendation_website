from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ReviewSerializer, MovieListSerializer, MovieDetailSerializer, GenreSerializer
from .models import Movie, Genre, Actor, MovieReview
# Create your views here.

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie.objects.prefetch_related('actors','genres','directors', 'ott_paths'), pk=movie_id)

    # movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieDetailSerializer(movie)

    is_liked = False

    if request.user:
        if movie.like_users.filter(pk=request.user.pk).exists():
            is_liked = True
        else:
            is_liked = False

    context = {
        'data': serializer.data,
        'is_liked': is_liked
    }

    return Response(context)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def review_list(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    review = movie.reviews.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(serializer.data)
