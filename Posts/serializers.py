from rest_framework import serializers

from .models import Post , Comment

class PostSerializer(serializers.ModelSerializer): # был Serializer
    class Meta:
        model = Post
        #fields = ('title', 'content', 'cat')
        fields = '__all__'

class ComentSerializer(serializers.ModelSerializer): # был Serializer
    class Meta:
        model = Comment
        fields = ('id', 'comment_text')
