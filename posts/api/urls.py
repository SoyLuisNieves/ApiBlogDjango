from django.urls import re_path, path
from django.contrib import admin

from .views import (
	PostDetailAPIView,
	PostListAPIView,
)

app_name = 'posts-api'

urlpatterns = [
	path('', PostListAPIView.as_view(), name='list'),
    re_path('(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name='detail'),

]