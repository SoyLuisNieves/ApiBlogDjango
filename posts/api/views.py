from rest_framework.generics import (
	DestroyAPIView,
	ListAPIView, 
	RetrieveAPIView,
	UpdateAPIView,
)

from posts.models import Post
from posts.api.serializers import PostDetailSerializer, PostListSerializer


# Detail Post
class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'
	# Slug field as id or pk in url
	# lookup_url_kwarg = 'abc'

class PostUpdateAPIView(UpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'


class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'

# All post
class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer
