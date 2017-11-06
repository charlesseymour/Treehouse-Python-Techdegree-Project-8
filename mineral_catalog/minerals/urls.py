from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mineral_list, name='list'),
    url(r'(?P<letter>[A-Z])/$', views.mineral_list, name='list'),
    url(r'(?P<pk>\d+)/$', views.mineral_detail, name='detail'),
    url(r'^group/(?P<group_name>[\w\ ]+)/$', views.mineral_group_list, name='group_list'),
    url(r'search/$', views.search, name='search')
]
