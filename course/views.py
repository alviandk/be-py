from django.shortcuts import get_object_or_404, render

from .models import Course, Module


def course_list_view(request):
    context = {}

    context['course_list'] = Course.objects.all()

    return render(request, 'learn/learn_text_list.html', context)


def course_detail_view(request, slug):
    context = {}

    context['course'] = get_object_or_404(Course, slug=slug)

    return render(request, 'learn/learn_text_detail.html', context)