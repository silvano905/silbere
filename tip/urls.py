from django.conf.urls import url
from tip import views


app_name = 'tips'

urlpatterns = [
    url(r'^$', views.tips_list_search, name='list'),
    url(r'^create_tip/$', views.crate_tip, name='create_tip'),
    url(r'^by/(?P<username>[-\w]+)/$', views.UserTips.as_view(), name='for_user'),
    # url(r'^by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='single'),

    # url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^tip/(?P<pk>\d+)/edit/$', views.TipUpdateView.as_view(), name='tip_edit'),
    url(r'^tip/(?P<pk>\d+)/remove/$', views.TipDeleteView.as_view(), name='tip_remove'),
    url(r'^crown/$', views.RequestCrown.as_view(), name='get_crown'),

    url(r'^tip/(?P<pk>\d+)$', views.tip_details, name='tip_detail'),
    url(r'^like/$', views.like_tip, name='like_tip'),
    url(r'^down/$', views.down_tip, name='down_tip'),
    url(r'^warning', views.CreateProfileBeforeSearch.as_view(), name='createprofilebeforeview'),

]