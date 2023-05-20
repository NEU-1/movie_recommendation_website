from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    # path('create_data/', views.create_data),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/reviews/', views.review_list),
    path('<int:movie_id>/reviews/create/', views.review_create),
    path('<int:movie_pk>/likes/', views.movie_likes),
    path('your-url/', views.your_view_function),
    path('genre/', views.genre),

]
