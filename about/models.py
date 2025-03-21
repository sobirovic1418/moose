from importlib.util import module_for_loader

from django.db import models

class About(models.Model):
    title=models.CharField(max_length=202)
    full_name=models.CharField(max_length=202)
    body_user=models.CharField(max_length=202)
    image=models.FileField(upload_to="about/")
    twitter=models.CharField(max_length=202)
    facebook=models.CharField(max_length=202)
    instagram=models.CharField(max_length=202)
    description=models.TextField()
    how_i_work=models.TextField()


    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.full_name