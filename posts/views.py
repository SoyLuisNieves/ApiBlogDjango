from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
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
    queryset_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list, 10)

    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "Post list is working!",
        "page_request_var": page_request_var
    }
    return render(request, "post_list.html", context)

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form =PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Item saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form
    }
    return render(request, "create_form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts:list")