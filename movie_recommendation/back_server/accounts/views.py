from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from .serializers import UserSerializer
from .models import User


def some_view_func(request):
    token = Token.objects.create(user=...)
    return Response({ 'token':token.key })

# 사용자의 ID로 사용자를 찾는 함수
def get_user(pk):
    return get_object_or_404(get_user_model(), pk=pk)

# 오류 메시지를 반환하는 함수
def error_response(message):
    return Response({'error': message})

# 사용자가 다른 사용자를 팔로우하거나 팔로우 취소하는 함수
def handle_follow(me, person):
    # 팔로우 목록에서 해당 사용자가 있는지 확인
    if me.followings.filter(pk=person.pk).exists():
        # 있으면 팔로우 취소
        me.followings.remove(person)
        return False
    else:
        # 없으면 팔로우
        me.followings.add(person)
        return True


@api_view(['GET'])  # GET 요청을 처리
# 특정 사용자의 프로필 정보를 반환하는 API endpoint
def profile(request, user_pk):
    # 요청된 pk를 가진 사용자 정보를 얻음
    user = get_user(user_pk)
    # 사용자 정보를 시리얼라이즈
    serializer = UserSerializer(user)
    # 시리얼라이즈 된 데이터 반환
    return Response(serializer.data)


@api_view(['POST'])
def follow(request, my_pk, user_pk):
    # 요청받은 사용자 객체를 불러옵니다.
    me = get_object_or_404(User, pk=my_pk)
    # 팔로우할 사용자 객체를 불러옵니다.
    person = get_object_or_404(User, pk=user_pk)

    # 팔로우 중인지 확인합니다.
    if me != person:
        if me in person.followers.all():  # 이미 팔로우 중이라면
            # 팔로우를 취소합니다.
            person.followers.remove(me)
            followed = False
        else:
            # 팔로우를 합니다.
            person.followers.add(me)
            followed = True

        follow_status = {'followed': followed}
        return Response(follow_status)

    return Response({'detail': "Can't follow yourself"})


# 팔로우 여부를 확인하는 함수
@api_view(['POST'])
def is_follow(request, my_pk, user_pk):
    # 요청으로부터 person과 me를 가져옴
    person = get_user(user_pk)  # 팔로우 대상 사용자
    me = get_user(my_pk)  # 요청한 사용자

    # 요청한 사용자와 팔로우 대상 사용자가 같지 않은지 확인
    if person != me:
        # 팔로우 여부를 확인하고 그 결과를 반환
        following = me.followings.filter(pk=person.pk).exists()
        return Response(following)
    else:
        # 같은 경우 에러 메시지 반환
        return error_response('자기 자신은 팔로우할 수 없습니다.')