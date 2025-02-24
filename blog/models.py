from django.db import models



class Tag(models.Model):
    title=models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title=models.CharField(max_length=202)
    image=models.FileField(upload_to="blog/")
    tag=models.ManyToManyField(Tag,related_name="tag")
    description=models.TextField()
    how_i_work = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="blog")
    email=models.EmailField()
    message=models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog
