from django.forms import UUIDField
from rest_framework import serializers
import datetime

from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from .models import Post,Comment





class CommentSerializer(serializers.ModelSerializer): # был Serializer
    pk = serializers.ReadOnlyField(source='id')
    class Meta:
        model = Comment
        fields = ('comment_text', 'pk')
        #fields = '__all__'




class PostSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        #comment_text = serializers.CharField(max_length=255)
        #comments = ComentSerializer().to_representation

        #fields = '__all__'
        fields = ('title', 'post_text', 'views_quantity', 'time_create')
        #fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance=instance)
        comment = Comment.objects.filter(post=instance).last()
        data['comments'] = CommentSerializer(instance=comment).data
        return data



class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ('title', 'post_text', 'views_quantity', 'time_create', 'comments')










