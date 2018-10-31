from django.shortcuts import render
from accounts.models import Profile
from .forms import MakeMessageGroupForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import GroupMessage
from django.contrib.auth import get_user_model
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
User = get_user_model()


@login_required
def add_member_to_message_group(request, pk):
    member = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = MakeMessageGroupForm(request.POST)
        if form.is_valid():
            user_message_group = form.save(commit=False)
            user_message_group.member = request.user.profiles
            user_message_group.user = member.user
            if_obj_exists = GroupMessage.objects.filter(member=member, user__exact=request.user).exists()
            if if_obj_exists:
                return redirect('accounts:detail', pk=pk)

            else:
                user_message_group.save()
                return redirect('accounts:detail', pk=pk)


class UserGroupMessages(ListView, LoginRequiredMixin):

    context_object_name = 'groupmessage_list'
    model = GroupMessage
    template_name = 'message_group/user_groupmessage_list.html'

    def get_queryset(self):
        try:
            self.owner_of_message_group = User.objects.prefetch_related('groupmessages').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.owner_of_message_group.groupmessages.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['friend_user'] = self.owner_of_message_group
        return context


@login_required
def delete(request, pk):
    query = GroupMessage.objects.filter(user__exact=request.user, member_id__exact=pk)
    query.delete()
    return redirect('group_message:my_message_members', username=request.user.username)

