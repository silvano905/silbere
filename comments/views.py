from django.shortcuts import render
from .forms import CommentForm
from tip.models import MakeTip
from .models import Comment
from django.shortcuts import render, get_object_or_404, redirect
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from notify.signals import notify


def add_comment_to_post(request, pk):
    post = get_object_or_404(MakeTip, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post     # Remember here that our Comment object has an attribute called post of type Post
            comment.author = request.user
            comment.save()

            notify.send(sender=request.user, actor=request.user, recipient=post.author,
                        verb="agrego un comentario a: ' {} ' ".format(post.title), nf_type='followed_by_one_user')


            return redirect('tips:tip_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'comments/comment_form.html', {'form': form})


