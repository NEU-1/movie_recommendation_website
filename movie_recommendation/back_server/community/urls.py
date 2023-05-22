from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('create/', views.create), 
    path('detail/<int:community_pk>/', views.community_detail), 
    path('update/<int:community_pk>/', views.community_update_delete),
    path('comments/<int:community_pk>', views.comment_list),
    path('<int:community_pk>/comment_create/', views.create_comment),
    path('comment/<int:community_pk>/<int:comment_pk>/', views.comment_update_delete),
]