from django.conf.urls import patterns, include, url
from deal import views
urlpatterns = patterns('',
	url(r'^user/', views.index),
	#url(r'^xiangxi/(?P<name_url>\w+)/$', views.category, name='category'),
	#url(r'^register/',views.register),
	url(r'^login/',views.login),
	url(r'^user/received/',views.received),
	url(r'^user/unreceipted/',views.unreceipted),
	url(r'^test/',views.test),
#	url(r'^main/',views.main),
)