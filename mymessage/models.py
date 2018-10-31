from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from accounts.models import Profile


class MyMessage(models.Model):
    author = models.ForeignKey(User, related_name='mymessages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField()
    picture = models.ImageField(upload_to='media', blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('message:for_user', kwargs={'username': self.author.username})

    def filter_by_id(self, obj):
        return obj.id

    class Meta:
        ordering = ['created_date']



