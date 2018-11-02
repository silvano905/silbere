from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from tip.models import MakeTip
from .forms import UserFormRegistration, UserFormProfile, UserFormCreationFormUpdate, UserFormProfileUpdate
from accounts.models import Profile, PointsUserList, BlockedList
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


class ViewUserProfile(TemplateView, LoginRequiredMixin):
    template_name = 'accounts/profile.html'


@login_required
def crate_user_profile(request):
    form = UserFormProfile()

    if request.method == "POST":
        form = UserFormProfile(data=request.POST, files=request.FILES)

        if form.is_valid():
            userprofile = form.save(commit=False)

            pic = form.cleaned_data['profile_pic']
            if not pic:
                userprofile.profile_pic = 'hummingbird.jpg'
            userprofile.user = request.user

            form.save(commit=True)

            return render(request, 'tip/tip_list.html')
        else:
            form = UserFormProfile()

    return render(request, 'accounts/profile.html', {'form': form})


def create_user_form(request):
    form = UserFormRegistration()

    if request.method == "POST":
        form = UserFormRegistration(request.POST)

        if form.is_valid():
            form.save(commit=False)
            email_user = form.cleaned_data['email']
            username = form.cleaned_data['username'].lower()
            form.username = username
            form.save(commit=True)

            msg_html = render_to_string('registration/welcome.html')
            send_mail('SILBERE', 'Bienvenido!', settings.EMAIL_HOST_USER, [email_user], html_message=msg_html,
                      fail_silently=False)
            return redirect('login')
        else:
            form = UserFormRegistration()

    return render(request, 'registration/form.html', {'form': form})


@login_required
def search_users(request):
    queryset_list = {}

    query = request.GET.get('q')
    if query is not None:
        queryset_list = Profile.objects.all().exclude(user=request.user)
        queryset_list = queryset_list.filter(
            Q(user__first_name=query) | Q(user__username=query) | Q(user__last_name=query) | Q(user__email=query))

    context = {
        "object_list": queryset_list
    }
    return render(request, 'search_users/index.html', context)


@login_required
def user_detail_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    is_admirador = False
    is_blocked = False

    if BlockedList.objects.filter(user=profile.user, profile=request.user.profiles):
        is_blocked = True

    if PointsUserList.objects.filter(user=request.user, profile=profile.pk):
        is_admirador = True

    context = {
        'is_blocked': is_blocked,
        'is_admirador': is_admirador,
        'user_list': profile,
        'post_list': MakeTip.objects.filter(author=profile.user),
    }
    return render(request, 'accounts/user_detail.html', context)


@login_required
def point_crown(request):
    is_admirador = False
    profile = get_object_or_404(Profile, id=request.POST.get('profile_pk'))
    membership = PointsUserList.objects.filter(user=request.user, profile=profile.pk)
    if membership:
        membership.delete()
        is_admirador = False

    else:
        PointsUserList.objects.create(user=request.user, profile=profile)
        is_admirador = True
    return redirect(profile.get_absolute_url())


@login_required
def edit_profile(request):
    image = request.user.profiles.profile_pic

    if request.method == 'POST':
        form1 = UserFormCreationFormUpdate(request.POST, instance=request.user)
        form2 = UserFormProfileUpdate(request.POST, request.FILES, instance=request.user.profiles)

        if form1.is_valid() and form2.is_valid():
            form1.save(commit=True)
            form2.save(commit=True)
            return redirect('tips:list')
    else:
        form1 = UserFormCreationFormUpdate(instance=request.user)
        form2 = UserFormProfileUpdate(instance=request.user.profiles)

    return render(request, 'accounts/createprofile.html', {'form': form1, 'formm': form2, 'image': image})


class UserProfileView(TemplateView, LoginRequiredMixin):
    template_name = 'accounts/view_profile.html'


class ConfirmDeactivate(TemplateView, LoginRequiredMixin):
    template_name = 'profile/confirm_deactivate.html'


@login_required
def delete_profile(request):
    user = request.user
    user.is_active = False
    user.save()
    messages.success(request, 'Perfil fue desactivado.')
    return redirect('tips:list')





