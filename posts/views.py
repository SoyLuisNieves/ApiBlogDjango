from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Success created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not success created")
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

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form =PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Item saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form
    }
    return render(request, "create_form.html", context)

def post_delete(request):
    return HttpResponse("Delete")