from django.conf.urls import url
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'accounts'

urlpatterns = [
    url(r'^registration/$', views.create_user_form, name='registration'),
    url(r'^$', views.search_users, name='list'),
    url(r'^profile/$', views.edit_profile, name='profile'),
    url(r'^craeateprofile$', views.crate_user_profile, name='createprofile'),
    url(r'^(?P<pk>\d+)/$', views.user_detail_view, name='detail'),
    url(r'^viewprofile/$', views.UserProfileView.as_view(), name='viewprofile'),
    url(r'^confirm-deactivate/$', views.ConfirmDeactivate.as_view(), name='confirm-deactivate'),
    url(r'^deactivate/$', views.delete_profile, name='deactivate'),
    url(r'^point/$', views.point_crown, name='point_crown'),
    url(r'^login/$', LoginView.as_view(), {'template_name': 'login.html'}, name='login'),

]