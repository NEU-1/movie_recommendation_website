from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('follow/<int:my_pk>/<int:user_pk>/', views.follow),
    path('users/', views.users),
    path('user/<int:my_pk>/', views.user),
    path('signup/', views.signup),
    path('myprofile/', views.my_profile),
    path('is_follow/<int:my_pk>/<int:user_pk>/', views.is_follow),
    path('api-token-auth/', obtain_jwt_token),
    path('info/', views.users_info),
    path('<int:user_pk>/', views.profile),
]


