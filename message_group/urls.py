from django.conf.urls import url
from message_group import views

app_name = 'group_message'

urlpatterns = [
    url(r'^add/(?P<pk>\d+)/to_friends_list/$', views.add_member_to_message_group, name='add_groupmessage_member'),
    url(r'^view_members/(?P<username>[-\w]+)/friends_list/$', views.UserGroupMessages.as_view(), name='my_message_members'),
    url(r'^remove/(?P<pk>\d+)/$', views.delete, name='member_remove'),

]