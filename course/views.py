from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .forms import CollegeProjectForm
from .models import Course, Module, Mentor
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
        college_project_form = CollegeProjectForm(request.POST)

        # Check if the form is valid:
        if user_profile_form.is_valid() and education_profile_form.is_valid() and college_project_form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            user_profile_form.save()
            education_profile_form.save()
            new_college_project_form = college_project_form.save(commit=False)
            new_college_project_form.user = request.user
            new_college_project_form.current_education = education_profile_instance
            new_college_project_form.save()
            from django.contrib import messages
            messages.success(
                request, 
                'Pengajuan bimbingan tugas akhir kamu sudah kami terima! Setelah mereview, \n kami akan menghubungi kamu.'
            )

    # If this is a GET (or any other method) create the default form.
    else:
        user_profile_form = UserProfileForm(instance=user_profile_instance)
        education_profile_form = EducationProfileForm(instance=education_profile_instance)
        
        college_project_form = CollegeProjectForm(initial={'target_month': timezone.now().date().month + 2})

    context = {
        'user_profile_form': user_profile_form,
        'education_profile_form': education_profile_form,
        'college_project_form': college_project_form
    }

    return render(request, 'learn/college_final_project.html', context)


def course_mentor_list_view(request):
    context = {}

    # context['course'] = get_object_or_404(Course, slug=slug)

    return render(request, 'learn/mentor_list.html', context)


def course_mentor_detail_view(request, id):
    context = {}

    context['mentor'] = get_object_or_404(Mentor, id=id)

    return render(request, 'learn/mentor_detail.html', context)


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
