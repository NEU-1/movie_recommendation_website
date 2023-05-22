from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('signup/', views.signup),
    path('myprofile/', views.my_profile),
    path('<int:user_pk>/', views.profile),
    path('follow/<int:my_pk>/<int:user_pk>/', views.follow),
    path('is_follow/<int:my_pk>/<int:user_pk>/', views.is_follow),
    path('api-token-auth/', obtain_jwt_token),
]


