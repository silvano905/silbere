from django.conf.urls import url
from mymessage import views

app_name = 'mymessage'

urlpatterns = [
    url(r'^add_message_to/(?P<pk>\d+)/$', views.make_a_message, name='add_message'),
    url(r'^list_messages/(?P<pk>\d+)/$', views.user_detail_messages_view, name='detail_messages'),
    url(r'^profile_block/$', views.block_user, name='block_user')

]