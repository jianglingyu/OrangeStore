#coding:utf8
from django import forms
from deal.models import Order,user
from django.contrib.auth.models import User


class OrderForm(forms.ModelForm):
	order_num = forms.CharField(max_length=128, label='订单号')
	order_date = forms.DateTimeField(label='订单日期')
	recieve_name = forms.CharField(max_length=128, label='收货人')
	recieve_addr  = forms.CharField(max_length=128, label='收货地址')
	recieve_pthon = forms.CharField(max_length=11, label='收货人联系方式')
	orange_kind = forms.CharField(max_length=50, label='水果种类')
	orange_weight = forms.IntegerField(label='购买重量')
	pay_name = forms.CharField(max_length=128, label='购买人')
	express_name = forms.CharField(max_length=128, label='快递类型')
	express_num = forms.CharField(max_length=128, label='快递单号')
	send_date = forms.DateTimeField(label='发货日期')
	note = forms.CharField(widget=forms.Textarea,label='备注')
	is_recieve = forms.NullBooleanField(label='是否已经签收')
	is_payed = forms.NullBooleanField(label='是否已经付款')
	recieve_date = forms.DateTimeField(label='签收日期')
	seller_user = forms.CharField()

	class Meta:
		model = Order

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'password')		

