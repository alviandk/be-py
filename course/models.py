from django.db import models

from ckeditor.fields import RichTextField


class Course(models.Model):
    course_name = models.CharField(max_length=256)
    description = models.TextField()
    cover_image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.course_name

class Module(models.Model):
    module_name = models.CharField(max_length=128)
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        related_name='modules'
    )

    def __str__(self):
        return f"course: {self.course.id}, module: {self.module_name}"

class ModuleContent(models.Model):
    text = RichTextField()
    module = models.ForeignKey(
        Module, 
        on_delete=models.CASCADE, 
        related_name='contents'
    )

    def __str__(self):
        return f"module: {self.module_name}, content: {self.id}, "
