"""taskproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.urls import path
from Posts.views import *

#router.register(r'Posts', PostsViewSet, basename='postlist')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/postlist/', PostsViewSet.as_view({'get': 'list'})),
    path('api/v1/postlist/<int:pk>/', PostsViewSet.as_view({'get': 'retrieve'})),
    path('api/v1/postlist/', PostsViewSet.as_view({'get': 'list'})),
    # path('api/v1/postlist/<int:pk>/', PostAPIUpdate.as_view()),
    # path('api/v1/postlist/', PostAPIList.as_view()),
    #path('api/v1/commentlist/', CommentViewSet.as_view({'get': 'list'}))
]
