from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics ,viewsets
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, PostDetailSerializer
from django.db.models import F
from rest_framework.response import Response






class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer





class PostsViewSet(viewsets.ModelViewSet):
    #queryset = Post.objects.all()
    #serializer_class = PostSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PostSerializer
        if self.action == 'retrieve':
            return PostDetailSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Post.objects.all()
        else:
            post = get_object_or_404(Post, pk=pk)
            #post = Post.objects.get(pk=pk)#.update(views_quantity = F("views_quantity") + 1)
            #post = post_to_save.first()
            #post_2 = Post.objects.filter(pk=pk)

            post.views_quantity = post.views_quantity + 1
            post.save()

            return Post.objects.filter(pk=pk)







