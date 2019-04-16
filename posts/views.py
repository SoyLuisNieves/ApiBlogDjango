from django.http import HttpResponse
from django.shortcuts import render

from .models import Post

def post_list(request):
    return HttpResponse("Home")

def post_create(request):
    return HttpResponse("Create")

def post_detail(request):
    return HttpResponse("Detail")

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