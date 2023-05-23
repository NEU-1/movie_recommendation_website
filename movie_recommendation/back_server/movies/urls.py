from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/reviews/', views.review_list),
    path('<int:movie_id>/reviews/create/', views.review_create),
    path('<int:movie_pk>/likes/', views.movie_likes),
    path('search/', views.search_movies),
    path('genre/', views.genre),

]
