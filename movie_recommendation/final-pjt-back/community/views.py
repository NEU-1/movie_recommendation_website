from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import CommunityListSerializer, CommentSerializer, CommunitySerializer, CommentListSerializer
from .models import Community


# 커뮤니티 pk를 받아 해당 커뮤니티를 반환하거나, 존재하지 않으면 404 에러를 반환하는 함수입니다.
def get_community(community_pk):
    return get_object_or_404(Community, pk=community_pk)


# 사용자, 인스턴스(커뮤니티 혹은 댓글), 인스턴스의 id를 받아 사용자의 권한을 확인하는 함수입니다.
# 해당 사용자가 인스턴스에 대한 권한이 없으면 에러 메시지를 반환합니다.
def check_user_permission(user, instance, instance_id):
    if not user.communities.filter(pk=instance_id).exists():
        return Response({'message': '권한이 없습니다.'})


# 커뮤니티 리스트를 조회(GET)하거나 새 커뮤니티를 생성(POST)하는 뷰
@api_view(['GET', 'POST'])
def create(request):
    # GET 요청일 경우
    if request.method == 'GET':
        communities = Community.objects.all()  # 모든 커뮤니티를 가져옵니다.
        serializer = CommunityListSerializer(communities, many=True)  # 커뮤니티 객체를 시리얼라이즈합니다.
        return Response(serializer.data)  # 시리얼라이즈된 데이터를 반환합니다.
    # POST 요청일 경우
    else:
        serializer = CommunitySerializer(data=request.data)  # 요청 데이터로 커뮤니티 시리얼라이저를 생성합니다.
        if serializer.is_valid(raise_exception=True):  # 요청 데이터가 유효한지 확인합니다.
            # 로그인 된 사용자인지 확인
            if not request.user.is_authenticated:
                return Response({'detail': '로그인이 필요한 서비스입니다.'}, status=status.HTTP_401_UNAUTHORIZED)
            serializer.save(user=request.user)  # 요청을 보낸 사용자를 사용자로 설정하여 커뮤니티를 저장합니다.
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # 저장된 커뮤니티 데이터와 생성된 상태 코드를 반환합니다.


# 특정 커뮤니티의 상세 정보를 조회하는 뷰입니다.
@api_view(['GET'])
def community_detail(request, community_pk):
    community = get_community(community_pk)  # 커뮤니티를 가져옵니다.
    serializer = CommunityListSerializer(community)  # 커뮤니티를 시리얼라이즈합니다.
    return Response(serializer.data)  # 시리얼라이즈된 커뮤니티 데이터를 반환합니다.


# 특정 커뮤니티에 달린 댓글 리스트를 조회하는 뷰입니다.
@api_view(['GET'])
def comment_list(request, community_pk):
    community = get_community(community_pk)  # 커뮤니티를 가져옵니다.
    comments = community.comment_set.all()  # 커뮤니티에 달린 모든 댓글을 가져옵니다.
    serializer = CommentListSerializer(comments, many=True)  # 댓글들을 시리얼라이즈합니다.
    return Response(serializer.data)  # 시리얼라이즈된 댓글 데이터를 반환합니다.


# 특정 커뮤니티에 댓글을 생성하는 뷰입니다.
@api_view(['POST'])
def create_comment(request, community_pk):
    community = get_community(community_pk)  # 커뮤니티를 가져옵니다.
    serializer = CommentSerializer(data=request.data)  # 요청 데이터로 댓글 시리얼라이저를 생성합니다.
    if serializer.is_valid(raise_exception=True):  # 요청 데이터가 유효한지 확인합니다.
        serializer.save(user=request.user, community=community)  # 요청을 보낸 사용자를 사용자로 설정하고 해당 커뮤니티에 댓글을 저장합니다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # 저장된 댓글 데이터와 생성된 상태 코드를 반환합니다.


# 커뮤니티를 업데이트(PUT)하거나 삭제(DELETE)하는 뷰입니다.
@api_view(['PUT', 'DELETE'])
def community_update_delete(request, community_pk):
    community = get_community(community_pk)  # 커뮤니티를 가져옵니다.
    permission_error = check_user_permission(request.user, community, community_pk)  # 사용자의 권한을 확인합니다.
    if permission_error:  # 권한 확인에서 에러가 발생하면 에러를 반환합니다.
        return permission_error
    
    if request.method == 'PUT':
        serializer = CommunitySerializer(community, data=request.data)  # 커뮤니티 시리얼라이저를 생성합니다.
        if serializer.is_valid(raise_exception=True):  # 요청 데이터가 유효한지 확인합니다.
            serializer.save(user=request.user)  # 요청을 보낸 사용자를 사용자로 설정하여 커뮤니티를 저장합니다.
            return Response(serializer.data)  # 저장된 커뮤니티 데이터를 반환합니다.
    else:
        community.delete()  # 커뮤니티를 삭제합니다.
        return Response({ 'id': community_pk })  # 삭제된 커뮤니티의 id를 반환합니다.


# 댓글을 업데이트(PUT)하거나 삭제(DELETE)하는 뷰입니다.
@api_view(['PUT', 'DELETE'])
def comment_update_delete(request, community_pk, comment_pk):
    community = get_community(community_pk)  # 커뮤니티를 가져옵니다.
    comment = community.comment_set.get(pk=comment_pk)  # 해당 커뮤니티에서 댓글을 가져옵니다.

    permission_error = check_user_permission(request.user, comment, comment_pk)  # 사용자의 권한을 확인합니다.
    if permission_error:  # 권한 확인에서 에러가 발생하면 에러를 반환합니다.
       return permission_error  # 권한 확인에서 에러가 발생하면 에러 메시지를 반환합니다.

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)  # 댓글 시리얼라이저를 생성합니다.
        if serializer.is_valid(raise_exception=True):  # 요청 데이터가 유효한지 확인합니다.
            serializer.save(user=request.user)  # 요청을 보낸 사용자를 사용자로 설정하여 댓글을 저장합니다.
            return Response(serializer.data)  # 저장된 댓글 데이터를 반환합니다.
    else:
        comment.delete()  # 댓글을 삭제합니다.
        return Response({ 'id': comment_pk })  # 삭제된 댓글의 id를 반환합니다.