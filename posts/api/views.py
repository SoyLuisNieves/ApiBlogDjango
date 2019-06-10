from rest_framework.generics import ListAPIView, RetrieveAPIView

from posts.models import Post
from posts.api.serializers import PostDetailSerializer, PostListSerializer


# Detail Post
class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	# lookup_field = 'slug'
	# Slug field as id or pk in url
	# lookup_url_kwarg = 'abc'

# All post
class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer