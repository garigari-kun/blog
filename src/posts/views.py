from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Post

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "title": "List",
        "object_list": queryset,
    }
    return render(request, 'index.html', context)

def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request, id):
    instance = get_object_or_404(Post, id = id)

    context = {
        "title": instance.title,
        "instance": instance,
    }

    return render(request, 'post_detail.html', context)

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
