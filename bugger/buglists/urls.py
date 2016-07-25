# buglists/urls.py
from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required

from . import views


urlpatterns = [
    url(r'^$', views.BuglistList.as_view(), name='buglist_list'),
    #url(r'^(?P<pk>\d+)/$', views.BuglistDetail.as_view(), name='buglist_detail'),
    url(r'^add/$', views.BuglistCreateView.as_view(), name='buglist_add'),
    url(r'^(?P<pk>\d+)/edit/$', views.BuglistUpdateView.as_view(), name='buglist_edit'),
    url(r'^tracker/add/$', views.BuglistTracker.as_view(), name='buglist_tracker'),
    url(r'^(?P<pk>\d+)/$', views.buglist_detail, name='buglist_detail'),
]