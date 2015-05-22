from django.conf.urls import url

from .. import views


urlpatterns = [
    url(r'^(?P<pk>[-\w]+)/$', views.GroupView.as_view(), name='group'),
]