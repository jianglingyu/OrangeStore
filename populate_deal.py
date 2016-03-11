import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dealInfo.settings')
import django
django.setup()

from deal.models import DealInfo

def populate():
	add_deal(num=101,recvName='jiao',buyer='jiang')
	add_deal(num=103,recvName='jiao1',buyer='jiang2')
	add_deal(num=106,recvName='jiao2',buyer='jiang3')
	add_deal(num=102,recvName='jiao3',buyer='jiang4')
	add_deal(num=104,recvName='jiao4',buyer='jiang5')

def add_deal(num,recvName,buyer):
	p = DealInfo.objects.get_or_create(num=num,recvName=recvName,buyer=buyer)[0]
	return p

if __name__ =='__main__':
	populate()	