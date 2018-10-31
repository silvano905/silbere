from accounts.models import Profile
from .forms import MakeFriendForm
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from .models import Friend
from django.contrib.auth import get_user_model
from django.http import Http404
from django.contrib import messages
from notify.signals import notify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
User = get_user_model()


@login_required
def add_friend_to_list(request, pk):
    friend = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = MakeFriendForm(request.POST)
        if form.is_valid():
            user_friend_list = form.save(commit=False)
            user_friend_list.friend = friend
            user_friend_list.user = request.user
            if_obj_exists = Friend.objects.filter(friend=friend, user__exact=request.user).exists()
            if if_obj_exists:
                messages.warning(request, '{} ya esta en tu lista de amigos!'.format(friend))
                return redirect('accounts:detail', pk=pk)

            else:

                notify.send(sender=request.user, actor=request.user, recipient=friend.user, verb='te agrego a la lista de amigos',
                            nf_type='followed_by_one_user')

                messages.success(request, '{} fue agregado a tus amigos!'.format(friend))
                user_friend_list.save()
                return redirect('accounts:detail', pk=pk)


class UserFriends(ListView, LoginRequiredMixin):

    context_object_name = 'friend_list'
    model = Friend
    template_name = 'friends/user_friend_list.html'

    def get_queryset(self):
        try:
            self.owner_of_friends = User.objects.prefetch_related('friends').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.owner_of_friends.friends.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['friend_user'] = self.owner_of_friends
        return context


@login_required
def delete(request, pk):
    query = Friend.objects.filter(user__exact=request.user, friend_id__exact=pk)
    query.delete()
    return redirect('friends:my_list_friend', username=request.user.username)
