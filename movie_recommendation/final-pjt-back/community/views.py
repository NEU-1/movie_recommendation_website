from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import CommunityListSerializer, CommentSerializer, CommunitySerializer, CommentListSerializer
from .models import Community


def get_community(community_pk):
    return get_object_or_404(Community, pk=community_pk)


def check_user_permission(user, instance, instance_id):
    if not user.communities.filter(pk=instance_id).exists():
        return Response({'message': '권한이 없습니다.'})


@api_view(['GET', 'POST'])
def create(request):
    if request.method == 'GET':
        communities = Community.objects.all()  
        serializer = CommunityListSerializer(communities, many=True)  
        return Response(serializer.data) 
    else:
        serializer = CommunitySerializer(data=request.data)  
        if serializer.is_valid(raise_exception=True):  
            if not request.user.is_authenticated:
                return Response({'detail': '로그인이 필요한 서비스입니다.'}, status=status.HTTP_401_UNAUTHORIZED)
            serializer.save(user=request.user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)  


@api_view(['GET'])
def community_detail(request, community_pk):
    community = get_community(community_pk)  
    serializer = CommunityListSerializer(community) 
    return Response(serializer.data) 


@api_view(['GET'])
def comment_list(request, community_pk):
    community = get_community(community_pk)  
    comments = community.comment_set.all() 
    serializer = CommentListSerializer(comments, many=True) 
    return Response(serializer.data)  


@api_view(['POST'])
def create_comment(request, community_pk):
    community = get_community(community_pk)  
    serializer = CommentSerializer(data=request.data) 
    if serializer.is_valid(raise_exception=True): 
        serializer.save(user=request.user, community=community) 
        return Response(serializer.data, status=status.HTTP_201_CREATED) 


@api_view(['PUT', 'DELETE'])
def community_update_delete(request, community_pk):
    community = get_community(community_pk) 
    permission_error = check_user_permission(request.user, community, community_pk) 
    if permission_error:  
        return permission_error
    
    if request.method == 'PUT':
        serializer = CommunitySerializer(community, data=request.data)  
        if serializer.is_valid(raise_exception=True):  
            serializer.save(user=request.user)  
    else:
        community.delete()  
        return Response({ 'id': community_pk }) 


@api_view(['PUT', 'DELETE'])
def comment_update_delete(request, community_pk, comment_pk):
    community = get_community(community_pk)  
    comment = community.comment_set.get(pk=comment_pk)  

    permission_error = check_user_permission(request.user, comment, comment_pk)  
    if permission_error:  
       return permission_error  

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)  
        if serializer.is_valid(raise_exception=True):  
            serializer.save(user=request.user) 
            return Response(serializer.data)  
    else:
        comment.delete()  
        return Response({ 'id': comment_pk }) 