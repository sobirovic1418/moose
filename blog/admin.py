from django.contrib import admin
from blog.models import Blog, Comment ,Tag

admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Comment)
