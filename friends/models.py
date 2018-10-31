from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Profile


class Friend(models.Model):
    user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    friend = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('friends:my_list_friend', kwargs={'username': self.user.username})

    class Meta:
        ordering = ['friend']
