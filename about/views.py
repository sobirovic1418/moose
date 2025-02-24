from django.shortcuts import render
from about.models import About


def about(request):
    about_me=About.objects.all()
    ctx={
        'about':about_me
    }
    return render(request,"about.html",ctx)