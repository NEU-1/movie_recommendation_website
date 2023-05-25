from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from .models import User


def some_view_func(request):
    token = Token.objects.create(user=...)
    return Response({ 'token':token.key })

def get_user(pk):
    return get_object_or_404(get_user_model(), pk=pk)

def error_response(message):
    return Response({'error': message})

def handle_follow(me, person):
    if me.followings.filter(pk=person.pk).exists():
        me.followings.remove(person)
        return False
    else:
        me.followings.add(person)
        return True


@api_view(['GET'])  
def profile(request, user_pk):
    user = get_user(user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def follow(request, my_pk, user_pk):
    me = get_object_or_404(User, pk=my_pk)
    person = get_object_or_404(User, pk=user_pk)

    if me != person:
        if me in person.followers.all(): 
            person.followers.remove(me)
            followed = False
        else:
            person.followers.add(me)
            followed = True
        follow_status = {'followed': followed}
        return Response(follow_status)
    return Response({'detail': "Can't follow yourself"})


@api_view(['POST'])
def is_follow(request, my_pk, user_pk):
    person = get_user(user_pk)  
    me = get_user(my_pk)  

    if person != me:
        following = me.followings.filter(pk=person.pk).exists()
        return Response(following)
    else:
        return error_response('자기 자신은 팔로우할 수 없습니다.')