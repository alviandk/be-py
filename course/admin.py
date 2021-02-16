from django.contrib import admin

from .models import Course, Module, ModuleContent, Syllabus


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

