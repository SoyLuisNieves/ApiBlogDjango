from django.contrib import admin
from django.urls import re_path

from .views import (
   comment_thread,
)

app_name='comments'
urlpatterns = [
    re_path(r'^(?P<id>\d+)/$', comment_thread, name='comment_thread')
    #url(r'^(?P<id>\d+)/delete/$', comment_delete),
]