from django.contrib import admin

from .models import (
    CollegeProject, Company, Course, 
    Education, Experience,
    LegalLogo,
    Mentor, MentoringRequest, Module, ModuleContent, 
    School, Syllabus
)


class ModuleInline(admin.StackedInline):
    model = Module

class SyllabusInline(admin.StackedInline):
    model = Syllabus

class ModuleContentInline(admin.StackedInline):
    model = ModuleContent

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [SyllabusInline, ModuleInline,]
    prepopulated_fields = {"slug": ("course_name",)}

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [ModuleContentInline,]
    prepopulated_fields = {"slug": ("module_name",)}

@admin.register(CollegeProject)
class CollegeProjectAdmin(admin.ModelAdmin):
    pass


class EducationInline(admin.StackedInline):
    model = Education

class ExperienceInline(admin.StackedInline):
    model = Experience

admin.site.register(Mentor)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(LegalLogo)
admin.site.register(School)
admin.site.register(Company)
admin.site.register(MentoringRequest)