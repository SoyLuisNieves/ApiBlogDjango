from django.urls import re_path, path
from django.contrib import admin

from .views import (
	PostDeleteAPIView,
	PostDetailAPIView,
	PostListAPIView,
	PostUpdateAPIView,
)

app_name = 'posts-api'

urlpatterns = [
	path('', PostListAPIView.as_view(), name='list'),
    re_path(r'^(?P<slug>[-\w]+)/$', PostDetailAPIView.as_view(), name='detail'),
    re_path(r'^(?P<slug>[-\w]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    re_path(r'^(?P<slug>[-\w]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
]