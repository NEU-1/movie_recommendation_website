from django.urls import path
from . import views
from .views import your_view_function

app_name = 'movies'
urlpatterns = [
    path('movie_list/', views.movie_list),
    # path('create_data/', views.create_data),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/reviews/', views.review_list),
    path('<int:movie_id>/reviews/', views.review_create),
    path('<int:movie_pk>/getmovielike/', views.get_likes),
    path('<int:movie_pk>/postmovielike/', views.likes),
    path('your-url/', views.your_view_function),

]
