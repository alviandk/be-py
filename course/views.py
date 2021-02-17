from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Course, Module
from user.forms import EducationProfileForm, UserProfileForm
from user.models import EducationProfile, UserProfile


def course_list_view(request):
    context = {}

    context['course_list'] = Course.objects.filter(show=True)

    return render(request, 'learn/learn_text_list.html', context)


def course_detail_view(request, slug):
    context = {}

    context['course'] = get_object_or_404(Course, slug=slug)

    return render(request, 'learn/learn_text_detail.html', context)


def course_group_list_view(request):
    context = {}

    # context['course'] = get_object_or_404(Course, slug=slug)

    return render(request, 'learn/group_list.html', context)


def course_group_detail_view(request, slug):
    context = {}

    # context['course'] = get_object_or_404(Course, slug=slug)

    return render(request, 'learn/group_detail.html', context)


@login_required
def course_college_final_project_view(request):
    
    user_profile_instance, created = UserProfile.objects.get_or_create(user=request.user)

    user_educations = EducationProfile.objects.filter(user=request.user)
    if user_educations:
        education_profile_instance = user_educations.last()
    else:
        education_profile_instance = EducationProfile.objects.create(user=request.user)
    

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        user_profile_form = UserProfileForm(request.POST, instance=user_profile_instance)
        education_profile_form = EducationProfileForm(request.POST, instance=education_profile_instance)

        # Check if the form is valid:
        if user_profile_form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            user_profile_form.save()

            # redirect to a new URL:
            # return HttpResponseRedirect(reverse('all-borrowed') )
    # If this is a GET (or any other method) create the default form.
    else:
        user_profile_form = UserProfileForm(instance=user_profile_instance)
        education_profile_form = EducationProfileForm(instance=education_profile_instance)

    context = {
        'user_profile_form': user_profile_form,
        'education_profile_form': education_profile_form,
    }

    return render(request, 'learn/college_final_project.html', context)


def course_mentor_list_view(request):
    context = {}

    # context['course'] = get_object_or_404(Course, slug=slug)

    return render(request, 'learn/mentor_list.html', context)


@login_required
def course_mentoring_private_view(request):
    context = {}

    # context['course'] = get_object_or_404(Course, slug=slug)

    return render(request, 'learn/mentoring_private.html', context)


@login_required
def module_detail_view(request, course_slug, slug):
    context = {}

    module = get_object_or_404(Module, course__slug=course_slug, slug=slug)
    context['module'] = module 
    context['course'] = module.course
    return render(request, 'learn/module_text_detail.html', context)
