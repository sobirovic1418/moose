from django.shortcuts import render
from.models import Blog,Tag,Comment


def index(request):
    return render(request,"index.html")


def blog(request):
    blog=Blog.objects.all()
    ctx={
        'blogs':blog
    }
    return render(request,"blog.html",ctx)

def detail(request,pk):
    blog=Blog.objects.get(id=pk)
    ctx={
        'blod':blog
    }
    return render(request,"blog-single.html",ctx)