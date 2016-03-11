from django.db import models
from django.contrib.auth.models import User

class DealInfo(models.Model):
	num = models.CharField(max_length=128,unique=True)
	recvName = models.CharField(max_length=128)
	buyer = models.CharField(max_length=128)

	def __unicode__(self):
		return self.num

# Create your models here.
