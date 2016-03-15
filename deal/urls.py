from django.conf.urls import patterns, include, url
from deal import views
urlpatterns = patterns('',
	url(r'^login/', views.login_view,name='login'),
	url(r'^order_detail/(?P<ordernumber>\w+)/$', views.select_OrderForm, name='select_OrderForm'),
	url(r'^update/(?P<id>\d+)/',views.update_OrderForm,name='update_OrderForm'),
	url(r'^add/', views.add, name='add'),
	url(r'^register/',views.register,name='register'),
	url(r'^received/',views.received),
	url(r'^unreceipted/',views.unreceipted),
	url(r'^allOrder/',views.allOrder),
	url(r'^logout', views.user_logout, name='logout'),
#	url(r'^main/',views.main),
)