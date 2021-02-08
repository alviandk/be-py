from django.db import models

from ckeditor.fields import RichTextField


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = RichTextField()
    url = models.URLField(blank=True, null=True)
    cover_image = models.ImageField()
    git_url = models.URLField()
    slug = models.SlugField(default="")
    ordering = models.IntegerField(default=0)

    def __str__(self):
        return self.name