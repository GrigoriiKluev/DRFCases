from django.test import TestCase
import pytest
from .models import Post
from .views import PostsViewSet
from rest_framework.test import APIClient
from mixer.backend.django import mixer


pytestmark = pytest.mark.django_db

class TestPostViewSet:

    # def setUp(self):
    #     self.client = APIClient() # Подключение тестирования запросов на URL

    def test_increase_views(self):
        last_post = Post.objects.create(
            title="Some title",
            post_text="Some_post_text",
        )
        #last_post = mixer.blend(Post)
        pre_quantity = last_post.views_quantity
        #print('pre_quantity', pre_quantity)
        response = APIClient().get("/api/v1/postlist/1/")
        print(response.json(), 'response_JSON')
        post_quantity = response.json()['views_quantity']
        #print(response.status_code , 'response_code')
        assert response.json != None
        assert response.status_code == 200
        #self.assertEqual(pre_quantity + 1, post_quantity)
        assert pre_quantity + 1 == post_quantity



    def test_create_post(self):
        # post_test = Post.objects.create(
        #     title="Some title",
        #     post_text = "Some_post_text",
        # )
        post_test = mixer.blend(Post, title='Some title') # Использование библиотеки миксер вместо создания обьекта
        post_result = Post.objects.last()

        #self.assertEqual(post_result.title, 'Some title')
        assert post_result.title == 'Some title'

