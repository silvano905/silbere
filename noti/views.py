from django.views.generic import ListView
from notify.models import Notification
from django.shortcuts import get_object_or_404, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class NotificationViewList(ListView, LoginRequiredMixin):
    template_name = 'noti/all.html'
    context_object_name = 'notifications'

    def dispatch(self, request, *args, **kwargs):
        return super(NotificationViewList, self).dispatch(
            request, *args, **kwargs)


class AllNotificationsList(NotificationViewList, LoginRequiredMixin):
    """
    Index page for authenticated user
    """

    def get_queryset(self):

        qset = self.request.user.notifications.filter(deleted=False)
        return qset


@login_required
def delete(request, pk):
    notification_id = pk

    notification = get_object_or_404(Notification, recipient=request.user, id=notification_id)
    notification.deleted = True
    notification.save()

    if settings.DJANGO_NOTIFICATIONS_CONFIG['SOFT_DELETE']:
        notification.deleted = True
        notification.save()
    else:
        notification.delete()

    return redirect('noti:all')
