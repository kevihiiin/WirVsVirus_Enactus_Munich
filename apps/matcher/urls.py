#-*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path

from . import views

app_name = "matcher"
urlpatterns = [
    # path(r'helper/', views.IndexView.as_view(), name='helper_index'),
    path(r'helper/new/', views.helper_new, name='helper_new'),
    path(r'helper/detail/<uuid:helper_id>', views.helper_detail, name='helper_detail'),
    # path(r'institution/', views.IndexView.as_view(), name='institution_index'),
    path(r'institution/new/', views.institution_new, name='institution_new'),
    path(r'institution/detail/<uuid:inquiry_id>', views.institution_detail, name='institution_detail'),
    # url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
]
