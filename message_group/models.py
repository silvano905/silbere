from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Profile
from django.utils import timezone


class GroupMessage(models.Model):
    user = models.ForeignKey(User, related_name='groupmessages', on_delete=models.CASCADE)
    member = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('friends:my_list_friend', kwargs={'username': self.user.username})

    class Meta:
        ordering = ['-created_date']
