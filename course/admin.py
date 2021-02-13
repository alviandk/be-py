from django.contrib import admin

from .models import Course, Module, ModuleContent


class ModuleInline(admin.StackedInline):
    model = Module

class ModuleContentInline(admin.StackedInline):
    model = ModuleContent

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInline,]
    prepopulated_fields = {"slug": ("course_name",)}

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [ModuleContentInline,]

