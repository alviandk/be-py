from django.db import models

from ckeditor.fields import RichTextField

from user.models import DplUser


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = RichTextField()
    url = models.URLField(blank=True, null=True)
    cover_image = models.ImageField()
    git_url = models.URLField()
    owner = models.ForeignKey(
            DplUser, 
            on_delete=models.CASCADE, 
            related_name='projects',
            null=True
    )
    slug = models.SlugField(default="")
    ordering = models.IntegerField(default=0)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.name