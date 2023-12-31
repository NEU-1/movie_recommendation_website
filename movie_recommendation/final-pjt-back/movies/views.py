import json
from .models import Movie
from django.http import JsonResponse
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework import status
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET'])
def movie_list(request):
    with open('movies/fixtures/movies.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return JsonResponse(data, safe=False)
  


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

    

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



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'GET':
        like_count = movie.like_users.count()
        return Response({'like_count': like_count})
    
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
        
    serializer = MovieSerializer(movie)
    return Response(serializer.data)



@api_view(['GET'])
def search_movies(request):
    q = request.GET.get('q', '')
    qs = Movie.objects.none()
    if q:
        qs = Movie.objects.filter(Q(title__icontains=q))
    serializer = MovieSerializer(qs, many=True)
    return Response(serializer.data)



def genre(request):
    with open('movies/fixtures/genre.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return JsonResponse(data, safe=False)

