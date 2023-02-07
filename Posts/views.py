from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics ,viewsets
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, ComentSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



# class PostsAPIView(APIView):
#     def get(self, request):
#         p = Post.objects.all()
#         serializer = PostSerializer(p, many=True)
#         our_posts = serializer.data
#         for i in range(len(our_posts)):
#             id = our_posts[i]['id']
#             comment = Comment.objects.filter(post_id=id)
#             comments_serializer = ComentSerializer(comment, many=True)
#             our_comments = comments_serializer.data
#
#
#         #coments = Comment.objects.filter()
#         return Response({'posts': our_posts, 'our_comments':our_comments})



