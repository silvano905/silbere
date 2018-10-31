from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

MY_CHOICES = (
    ('mujer', 'mujer'),
    ('hombre', 'hombre')
)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profiles', on_delete=models.CASCADE)
    gender = models.CharField(max_length=7, choices=MY_CHOICES)
    description = models.TextField(max_length=200)
    profile_pic = models.ImageField(upload_to='media', blank=True)
    rey_reina = models.BooleanField(default=False)
    points = models.ManyToManyField('auth.User', related_name='puntos', blank=True, through='PointsUserList')
    blocked_users = models.ManyToManyField('auth.User', related_name='blocked', blank=True, through='BlockedList')

    def __str__(self):
        return self.user.username

    def total_points(self):
        return self.points.count()

    def get_absolute_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.pk})


class PointsUserList(models.Model):
    profile = models.ForeignKey(Profile, related_name='admiradores', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class BlockedList(models.Model):
    profile = models.ForeignKey(Profile, related_name='members', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
