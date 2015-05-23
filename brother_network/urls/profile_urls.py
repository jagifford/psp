from django.conf.urls import url

from .. import views


urlpatterns = [
    url(r'^$', views.ProfileView.as_view(), name='blank_profile'),
    url(r'^(?P<slug>[-\w]+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'^(?P<slug>[-\w]+)/groups/$', views.GroupsView.as_view(), name='groups'),
]
