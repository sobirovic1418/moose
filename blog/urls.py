from xml.etree.ElementInclude import include
from django.urls import path
from blog.views import index,blog,detail

urlpatterns=[
    path('',index),
    path('blog/',blog),
    path('blog/detail/<int:pk>/',detail)
]