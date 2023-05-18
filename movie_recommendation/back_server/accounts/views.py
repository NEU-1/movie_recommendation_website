from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from .serializers import UserSerializer

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



@api_view(['POST'])  # POST 요청을 처리
# 사용자 등록을 위한 API endpoint
def signup(request):
    # 클라이언트에서 보낸 비밀번호 정보 받기
    password = request.data.get('password')
    # 클라이언트에서 보낸 비밀번호 확인 정보 받기
    passwordConfirmation = request.data.get('passwordConfirmation')
    # 비밀번호 일치 여부 확인
    if password != passwordConfirmation:
        # 일치하지 않을 경우 에러 메시지 반환
        return error_response('비밀번호가 일치하지 않습니다.')
    else:
        # 사용자가 보낸 데이터로 UserSerializer를 통해 데이터 생성
        serializer = UserSerializer(data=request.data)
        # 시리얼라이저의 유효성 검사
        if serializer.is_valid(raise_exception=True):
            # 사용자 저장. 이 시점에서는 비밀번호가 암호화되지 않았음
            user = serializer.save()
            # 비밀번호 암호화
            user.set_password(request.data.get('password'))
            user.save()
            # 사용자 데이터 반환
            return Response(serializer.data)
        

@api_view(['POST'])  # POST 요청을 처리
@authentication_classes([JSONWebTokenAuthentication])  # JWT 인증 사용
@permission_classes([IsAuthenticated])  # 인증된 사용자만 요청 가능
# 로그인된 사용자의 프로필 정보를 반환하는 API endpoint
def my_profile(request):
    # 요청된 사용자 정보를 얻음
    user = get_user(request.data.get('user_id'))
    # 사용자 정보를 시리얼라이즈
    serializer = UserSerializer(user)
    # 시리얼라이즈 된 데이터 반환
    return Response(serializer.data)


@api_view(['GET'])  # GET 요청을 처리
# 특정 사용자의 프로필 정보를 반환하는 API endpoint
def profile(request, user_pk):
    # 요청된 pk를 가진 사용자 정보를 얻음
    user = get_user(user_pk)
    # 사용자 정보를 시리얼라이즈
    serializer = UserSerializer(user)
    # 시리얼라이즈 된 데이터 반환
    return Response(serializer.data)


# 팔로우 요청을 처리하는 함수
@api_view(['POST'])
def follow(request, my_pk, user_pk):
    # 요청으로부터 person과 me를 가져옴
    person = get_user(user_pk)  # 팔로우 대상 사용자
    me = get_user(my_pk)  # 요청한 사용자

    # 요청한 사용자와 팔로우 대상 사용자가 같지 않은지 확인
    if person != me:
        # 팔로우 상태를 변경하고 변경된 상태를 반환
        following = handle_follow(me, person)
        return Response(following)
    else:
        # 같은 경우 에러 메시지 반환
        return error_response('자기 자신을 팔로우할 수 없습니다.')


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
        return error_response('자기 자신을 팔로우할 수 없습니다.')