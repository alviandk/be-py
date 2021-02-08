from django.shortcuts import render

from .forms import ContactMessageForm

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
        
    context['stories'] = MemberStory.objects.all()[:3]
    context['project_list'] = Project.objects.all()[:3]

    return render(request, 'home.html', context)