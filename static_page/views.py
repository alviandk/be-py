from django.shortcuts import render

from .forms import ContactMessageForm

from be_py.utils import sample_from_models
from portfolio.models import Project
from testimonial.models import MemberStory


def contact_us_view(request):
    context = {}
    form = ContactMessageForm()
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            context['message_status'] = 'saved'
        
    context['form'] = form

    return render(request, 'static_page/contact_us.html', context)


def home_view(request):
    context = {}
    
    stories_ids = sample_from_models(MemberStory, 3)
    projects_ids = sample_from_models(Project, 3)
    context['stories'] = MemberStory.objects.filter(id__in=stories_ids)
    context['project_list'] = Project.objects.filter(id__in=projects_ids)

    return render(request, 'home.html', context)