from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('movie_list/', views.movie_list),
    # path('create_data/', views.create_data),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/reviews/', views.review_list),
    path('<int:movie_id>/reviews/', views.review_create),
    
]
