from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class MakeTip(models.Model):
    author = models.ForeignKey(User, related_name='tips', on_delete=models.CASCADE)
    title = models.CharField(max_length=63)
    post_pic = models.ImageField(upload_to='media', blank=True)
    info = models.TextField(max_length=3000, blank=True)
    likes = models.ManyToManyField('auth.User', related_name='likes', blank=True, through='LikeUserList')
    down_votes = models.ManyToManyField('auth.User', related_name='downvotes', blank=True, through='DownVoteUserList')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def total_down_votes(self):
        return self.down_votes.count()

    def post_info_summary(self):
        len_info = len(self.info)
        if len_info > 480:
            return self.info[:480]+' . . . .continue'
        else:
            return self.info

    def get_absolute_url(self):
        return reverse('tips:tip_detail', kwargs={'pk': self.pk})



class LikeUserList(models.Model):
    post = models.ForeignKey(MakeTip, related_name='members', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class DownVoteUserList(models.Model):
    post = models.ForeignKey(MakeTip, related_name='members_down', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username