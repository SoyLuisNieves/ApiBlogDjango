from posts.models import Post
from posts.api.serializers import PostDetailSerializer

data = {
	"title": "New item",
	"content": "New content",
	"publish": "2019-06-06",
	"slug": "new-item",
}

# Get object
obj = Post.object.get(id=2)
new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
	new_item.save()
else:
	print(new_item.errors)

# Show new item
obj.data

# DELETE NEW ITEM
obj.delete()