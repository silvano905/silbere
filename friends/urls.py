from django.conf.urls import url
from friends import views

app_name = 'friends'

urlpatterns = [
    url(r'^add/(?P<pk>\d+)/to_friends_list/$', views.add_friend_to_list, name='add_friend'),
    url(r'^view/(?P<username>[-\w]+)/friends_list/$', views.UserFriends.as_view(), name='my_list_friend'),
    url(r'^remove/(?P<pk>\d+)/$', views.delete, name='friend_remove'),

]