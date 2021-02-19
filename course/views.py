from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .forms import CollegeProjectForm, MentoringRequestForm
from .models import CollegeProject, Course, Module, Mentor, MentoringRequest
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
    context = {}
    
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
            context['hidden_button'] = True
            
            messages.success(
                request, 
                'Pengajuan bimbingan tugas akhir kamu sudah kami terima! Kami akan menghubungi kamu, setelah kami selesai mereview.'
            )

    # If this is a GET (or any other method) create the default form.
    else:
        user_profile_form = UserProfileForm(instance=user_profile_instance)
        education_profile_form = EducationProfileForm(instance=education_profile_instance)
        college_project_form = CollegeProjectForm(initial={'target_month': timezone.now().date().month + 2})

        waiting_project_approval = CollegeProject.objects.filter(
            user=request.user, 
            status='WTG',
        )
        if waiting_project_approval:
            context['waiting_project_approval'] = True

    
    context['user_profile_form'] = user_profile_form,
    context['education_profile_form'] = education_profile_form,
    context['college_project_form'] = college_project_form

    return render(request, 'learn/college_final_project.html', context)


def course_mentor_list_view(request):
    context = {}

    context['mentors'] = Mentor.objects.all()

    return render(request, 'learn/mentor_list.html', context)


@login_required
def course_mentor_detail_view(request, id):
    context = {}

    context['mentor'] = get_object_or_404(Mentor, id=id)

    return render(request, 'learn/mentor_detail.html', context)


@login_required
def course_mentoring_private_view(request, id):
    context = {}
    user_profile_instance, created = UserProfile.objects.get_or_create(user=request.user)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        user_profile_form = UserProfileForm(request.POST, instance=user_profile_instance)
        mentoring_request_form = MentoringRequestForm(request.POST)

        if user_profile_form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            user_profile_form.save()
            mentoring_request = mentoring_request_form.save(commit=False)
            mentoring_request.mentor_id = id
            mentoring_request.user = request.user
            mentoring_request.save()

            context['hidden_button'] = True
            
            messages.success(
                request, 
                'Pengajuan mentoring private dari kamu sudah kami terima! \n Kami akan menghubungi kamu, setelah mentor merespon.'
            )
    else:
        user_profile_form = UserProfileForm(instance=user_profile_instance)
        mentoring_request_form = MentoringRequestForm()
        waiting_mentoring_requests = MentoringRequest.objects.filter(
            user=request.user, 
            status='WTG',
            mentor_id=id
        )
        if waiting_mentoring_requests:
            context['waiting_response'] = True

    context['mentor'] = get_object_or_404(Mentor, id=id)
    context['user_profile_form'] = user_profile_form
    context['mentoring_request_form'] = mentoring_request_form

    return render(request, 'learn/mentoring_private.html', context)


@login_required
def module_detail_view(request, course_slug, slug):
    context = {}

    module = get_object_or_404(Module, course__slug=course_slug, slug=slug)
    context['module'] = module 
    context['course'] = module.course
    return render(request, 'learn/module_text_detail.html', context)
