from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post

def post_list(request):
    return HttpResponse("Home")

def post_create(request):
    return HttpResponse("Create")

def post_detail(request, id=None):
    queryset = get_object_or_404(Post, id=id)
    context_data = {
        "queryset": queryset,
        "title": "Detail post"
    }
    return render(request, "post_detail.html", context_data)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "Post list is working!"
    }
    return render(request, "index.html", context)

def post_update(request):
    return HttpResponse("Update")

def post_delete(request):
    return HttpResponse("Delete")