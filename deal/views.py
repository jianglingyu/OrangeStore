# coding:utf-8
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import string
import random
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse

from deal.models import OrangeKind, Expresskind, Order

from django.http import JsonResponse
import json

from django.contrib.auth.decorators import login_required
from deal.forms import UserForm


fontPath = "./static/fonts/"


def index(request):
	context = RequestContext(request)
	top_list = Order.objects.order_by('-order_date')
	context_dict = {'orders': top_list}
	print top_list
	print context_dict
	return render_to_response('deal/main.html', context_dict)

#def received(request):





def category(request, name_url):
	name_dict = {'name_url':name_url}
	return render(request,'deal/login.html',name_dict)




# 获取4个随机数字母
def getRandomChar():
	return [random.choice(string.letters) for _ in range(4)]	
# 获得颜色
def getRandomColor():
	return (random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
# 获得验证码图片
def getCodePiture():
	width = 240
	height = 60
	# 创建画布
	image = Image.new('RGB', (width, height), (180,180,180))
	font = ImageFont.truetype(fontPath + 'gargi.ttf', 40)
	draw = ImageDraw.Draw(image)
	# 创建验证码对象
	code = getRandomChar()
	# 把验证码放到画布上
	for t in range(4):
		draw.text((60 * t + 10, 10), code[t],font=font,fill=getRandomColor())
	# 填充噪点
	for _ in range(random.randint(1500,3000)):
		draw.point((random.randint(0,width), random.randint(0,height)), fill=getRandomColor())
	# 模糊处理
	image = image.filter(ImageFilter.BLUR)
	# 保存名字为验证码的图片
	image.save("./static/images/check" + '.png', 'png')

def received(request,max_results=0, starts_with=' '):
	cat_list = Order.objects.filter(is_recieve=True).order_by('-order_date')
	context_dict = {'orders': cat_list}
#	return HttpResponse(json.dumps(test_dict), content_type='application/json')	
	return render(request,'deal/table.html',context_dict)


def unreceipted(request):
	cat_list = Order.objects.filter(is_recieve=False).order_by('-order_date')
	context_dict = {'orders': cat_list}
#	return HttpResponse(json.dumps(test_dict), content_type='application/json')	
	return render(request,'deal/table.html',context_dict)

def allOrder(request):
	cat_list = Order.objects.order_by('-order_date')
	context_dict = {'orders': cat_list}
#	return HttpResponse(json.dumps(test_dict), content_type='application/json')	
	return render(request,'deal/table.html',context_dict)	


from deal.forms import OrderForm
def select_OrderForm(request, ordernumber):
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print form.errors
	else:
		t = Order.objects.get(order_num=ordernumber)
		form = OrderForm(
			initial={'order_num': t.order_num,'order_date':t.order_date,
				 'recieve_name':t.recieve_name,'recieve_addr':t.recieve_addr,
				'recieve_pthon':t.recieve_pthon, 'orange_kind':t.orange_kind,
				'orange_weight':t.orange_weight, 'pay_name':t.pay_name,
				'express_name':t.express_name, 'express_num':t.express_num,
				'send_date':t.send_date, 'note':t.note,
				'is_recieve':t.is_recieve,'is_payed':t.is_payed,
				'recieve_date':t.recieve_date})
		return render(request, 'deal/select.html', {'form':form, 'order_num':t.id})


def update_OrderForm(request, id):
	blog = get_object_or_404(Order, pk=int(id))
	if request.method == 'POST':
		form = OrderForm(request.POST, instance=blog)
		if form.is_valid():
			form.save()
			return index(request)
		else:
			print form.errors
	else:
		return index(request)	


@login_required
def homepage(request):
	return render(request,"deal/myhome.html")

def login_view(request):
	if request.method == 'POST':
		print "post"
		username = request.POST.get('username')
		password = request.POST.get('password')
		print username
		print password
		user = authenticate(username=username, password=password)
		print "sadgagffsga"
		print user
		if user:
			if user.is_active:
				print "is active"
				login(request,user)
				print "login"
				top_list = Order.objects.order_by('-order_date')
				context_dict = {'orders': top_list}
				return render(request,'deal/myhome.html',context_dict)
				#return HttpResponse("sadgdashhgs")
			else:
				return HttpResponse("Your  account is disabled.")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		print "not post"
		return render(request, 'deal/login.html', {})
def selectAll(request):
	top_list = Order.objects.order_by('-order_date')
	context_dict = {'orders': top_list}


def register(request):
	registered = False
	if request.method == 'POST':
		#get form data
		username = request.POST.get('username')
		password = request.POST.get('password')
		passwordAgain  = request.POST.get("passwordAgain")
		print username
		print password

		#密码比较
		if password == passwordAgain:
			print "bbbbb"
			#user_form = UserForm(initial={'username': username,'password':password})
			user_form = UserForm(request.POST)
			#myuser_form = userform(request.POST)
			#if myuser_form.is_valid():
			#	print "myuser"
			if user_form.is_valid():
			#and myuser_form.is_valid():
				print "cccccc"

				user = user_form.save()
				user.set_password(user.password)
				user.save()
				#user.set_password(user.password)
				#myuser = myuser_form.save(commit=False)
				#myuser.save()

				top_list = Order.objects.order_by('-order_date')
				context_dict = {'orders': top_list}
				return render(request,"deal/login.html")
			else:
				print user_form.errors
		else:
			return HttpResponse("mimabuyizhi!")

	else:
		return render(request,"deal/register.html")

@login_required
def user_logout(request):
	logout(request)
	return render(request,"deal/login.html")		