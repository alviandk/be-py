from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Course, Module


def course_list_view(request):
    context = {}

    context['course_list'] = Course.objects.filter(show=True)

    return render(request, 'learn/learn_text_list.html', context)


def course_detail_view(request, slug):
    context = {}

    context['course'] = get_object_or_404(Course, slug=slug)

    return render(request, 'learn/learn_text_detail.html', context)


@login_required
def module_detail_view(request, course_slug, slug):
    context = {}

    module = get_object_or_404(Module, course__slug=course_slug, slug=slug)
    context['module'] = module 
    context['course'] = module.course
    return render(request, 'learn/module_text_detail.html', context)
