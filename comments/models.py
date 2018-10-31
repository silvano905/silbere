from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.db import models
# from tip.models import MakePost


class Comment(models.Model):
    post = models.ForeignKey('tip.MakeTip', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, max_length=200, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False) #default is that I have not approved the comment yet

                                                          # this approved_comment is used in the function approve_comments, under the filter
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('tips:list')

    def filter_by_id(self, obj):
        return obj.id

