# coding:utf-8
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import string
import random
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse

from deal.models import OrangeKind, Expresskind, Order

fontPath = "./static/fonts/"


def index(request):
	context = RequestContext(request)
	top_list = Order.objects.order_by('-order_date')

	context_dict = {'orders': top_list}

	cat_list = received()

	return render_to_response('deal/main.html', context_dict)

#def received(request):
def received(max_results=0, starts_with=' '):
	cat_list = Order.objects.filter(is_recieve=True).order_by('-order_date')
	context_dict = {'orders': cat_list}
	print "helloworld"
	return HttpResponse("context_dict")
#        	print context_dict

#        	return  context_dict

def unreceipted(request):
	data_list = Order.objects.filter(is_recieve=False).order_by('-order_date')
	print '*************************'
	print data_list
	return HttpResponse(data_list)

def category(request, name_url):
	return render(request,'deal/login.html')

def register(request):
    	return render(request,'deal/register.html')

def login(request):
	getCodePiture()
	return render(request,'deal/login.html')



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
	


def test(request):
	context = RequestContext(request)
	top_list = Order.objects.order_by('-order_date')

	context_dict = {'orders':top_list}
	return render_to_response('deal/test.html',context_dict)
