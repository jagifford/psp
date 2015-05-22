"""
PSP Network URL Configuration

"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^account/', include('brother_network.urls.account_urls', namespace='account')),
    url(r'^profile/', include('brother_network.urls.profile_urls', namespace='profile')),
    url(r'^group/', include('brother_network.urls.group_urls', namespace='group')),
]
