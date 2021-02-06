from django.shortcuts import render

# from .models import Project


def portfolio_list_view(request):
    context = {}

    # context['project_list'] = Project.objects.all()

    return render(request, 'portfolio/portfolio_list.html', context)