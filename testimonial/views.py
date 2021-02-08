from django.shortcuts import get_object_or_404, render

from .models import MemberStory


def testimonial_list_view(request):
    context = {}

    context['stories'] = MemberStory.objects.all()

    return render(request, 'testimonial/testimonial_list.html', context)


def testimonial_detail_view(request, testimonial_id):
    context = {}

    context['story'] = get_object_or_404(MemberStory, id=testimonial_id)

    return render(request, 'testimonial/testimonial_detail.html', context)