from django.shortcuts import render, redirect
from .forms import  ContactForm


def contact(request, POST=None):
    form=ContactForm(request,POST or None)
    if form.is_valed():
        form.save()
        return redirect('.')
    ctx={
        'form':form
    }

    return render(request,"contact.html",ctx)