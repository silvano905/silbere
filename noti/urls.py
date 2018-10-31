from django.conf.urls import url
from noti import views
app_name = 'noti'

urlpatterns = [
    url(r'^$', views.AllNotificationsList.as_view(), name='all'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete')
]