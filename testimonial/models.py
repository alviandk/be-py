from django.db import models

from ckeditor.fields import RichTextField

from user.models import DplUser


class MemberStory(models.Model):
    user = models.ForeignKey(
            DplUser, 
            on_delete=models.CASCADE, 
            related_name='stories'
    )
    story = RichTextField()

    def __str__(self):
        return f"{self.user.email}'s story"
