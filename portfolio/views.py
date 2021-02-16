from django.shortcuts import render

from .models import Project


def portfolio_list_view(request):
    context = {}

    context['project_list'] = Project.objects.filter(show=True)

    return render(request, 'portfolio/portfolio_list.html', context)


def project_detail_view(request, slug):
    context = {}

    context['project'] = Project.objects.get(slug=slug)

    return render(request, 'portfolio/portfolio_detail.html', context)
