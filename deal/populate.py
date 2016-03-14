import os
os.environ.setdefault('DJANGO_SETINGS_MODULE','dealInfo.settings')
import django
django.setup()

from deal.models import Order

def populate():

def add_order(order_num,order_date,receive_name,receive_pthon,orange_kind,orange_weight
			pay_name,express_name,express_num,send_date,note,is_receive,is_payed,receive_date):
	p = Order.objects.get_or_create((order_num=order_num,
					order_date=order_date,
					receive_name=receive_name,
					receive_pthon=receive_pthon,
					orange_kind=orange_kind,
					orange_weight=orange_weight,
					pay_name=pay_name,
					express_name=express_name,
					express_num=express_num,
					send_date=send_date,
					note=note,
					is_receive=is_receive,
					is_payed=is_payed,
					receive_date=receive_date)
	return p
