from uuid import uuid1

from django.db import models

from ckeditor.fields import RichTextField

from user.models import DplUser



class Course(models.Model):
    course_name = models.CharField(max_length=256)
    description = models.TextField()
    cover_image = models.ImageField()
    slug = models.SlugField()
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name


class Syllabus(models.Model):
    course = models.OneToOneField(
            Course, 
            on_delete=models.CASCADE, 
            related_name='syllabus'
    )
    objectives = RichTextField()
    technologies = RichTextField()
    prerequisites = RichTextField()
    version = models.CharField(max_length=8)
    last_change = models.DateField(null=True)
    author = models.ForeignKey(
        DplUser, 
        on_delete=models.CASCADE, 
        related_name='syllabus',
        null=True
    )
    source = RichTextField()
    

    def __str__(self):
        return f'syllabus: {self.course.course_name}'


class Module(models.Model):
    module_name = models.CharField(max_length=128)
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        related_name='modules'
    )
    slug = models.SlugField(null=True)

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
        return f"module: {self.module.module_name}, content: {self.id}, "

class CollegeProject(models.Model):
    user = models.ForeignKey(
            DplUser, 
            on_delete=models.CASCADE, 
            related_name='college_projects'
    )

    field_study = models.CharField(max_length=128, null=True)
    university_name = models.CharField(max_length=128, null=True)
    current_semester = models.PositiveIntegerField(null=True)


    def __str__(self):
        return f"{self.user.profile.name}'s colege project"