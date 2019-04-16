from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        
    context_data = {
        "form": form,
    }
    return render(request, "create_form.html", context_data)

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