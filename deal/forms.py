#coding:utf8
from django import forms
from deal.models import Order,user, OrangeKind, Expresskind
from django.contrib.auth.models import User


class OrderForm(forms.ModelForm):
	order_num = forms.CharField(label='订单号', widget=forms.TextInput(attrs={'readonly':'true'}))
	order_date = forms.DateTimeField(label='订单日期')
	recieve_name = forms.CharField(label='收货人')
	recieve_addr  = forms.CharField(label='收货地址')
	recieve_pthon = forms.CharField(label='收货人联系方式')
	orange_kind = forms.ModelChoiceField(queryset=OrangeKind.objects.all(), label='水果种类')
	orange_weight = forms.IntegerField(label='购买重量')
	pay_name = forms.CharField(label='购买人')
	express_name = forms.ModelChoiceField(queryset=Expresskind.objects.all(), label='快递类型')
	express_num = forms.CharField( label='快递单号')
	send_date = forms.DateTimeField(label='发货日期')
	note = forms.CharField(widget=forms.Textarea,label='备注')
	is_recieve = forms.NullBooleanField(label='是否已经签收')
	is_payed = forms.NullBooleanField(label='是否已经付款')
	recieve_date = forms.DateTimeField(label='签收日期')
	seller_user = forms.CharField(label='用户', widget=forms.TextInput(attrs={'readonly':'true'}))

	class Meta:
		model = Order
		fields = ('order_num', 'order_date', 'recieve_name', 'recieve_addr', 
			'recieve_pthon', 'orange_kind', 'orange_weight', 'pay_name', 'express_name', 
			'express_num', 'send_date', 'note', 'is_recieve', 'is_payed', 'recieve_date', 'seller_user')

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'password')		

