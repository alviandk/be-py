from django.shortcuts import render

# from .models import Project


def testimonial_list_view(request):
    context = {}

    # context['project_list'] = Project.objects.all()

    return render(request, 'testimonial/testimonial_list.html', context)


def testimonial_detail_view(request):
    context = {}

    # context['project_list'] = Project.objects.all()

    return render(request, 'testimonial/testimonial_detail.html', context)