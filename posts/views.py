from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_list(request):
    return HttpResponse("Home")

def post_create(request):
    return HttpResponse("Create")

def post_detail(request):
    return HttpResponse("Detail")

def post_list(request):
    return HttpResponse("List")

def post_update(request):
    return HttpResponse("Update")

def post_delete(request):
    return HttpResponse("Delete")