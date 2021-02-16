from django.db import models

from ckeditor.fields import RichTextField

from user.models import DplUser


class MemberStory(models.Model):
    user = models.ForeignKey(
            DplUser, 
            on_delete=models.CASCADE, 
            related_name='stories'
    )
    synopsis = models.CharField(max_length=128, default='')
    story = RichTextField()
    show = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.email}'s story"

    class Meta:
        ordering = ["order"]
