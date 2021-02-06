from django.shortcuts import render

# from .models import Project


def course_list_view(request):
    context = {}

    # context['project_list'] = Project.objects.all()

    return render(request, 'learn/learn_text_list.html', context)