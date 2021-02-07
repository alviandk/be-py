from django.shortcuts import render

from .forms import ContactMessageForm


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
