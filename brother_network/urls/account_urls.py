from django.conf.urls import url

from .. import views


urlpatterns = [
    url(r'^$', views.AccountView.as_view(), name='account'),
    url(r'^update/$', views.UpdateAccountView.as_view(), name='update'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]
