from django.conf.urls import url
from comments import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'comments'

urlpatterns = [
    url(r'^tip/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),

]
