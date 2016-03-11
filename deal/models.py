from django.db import models

# Create your models here.


class OrangeKind(models.Model):
    orange_kind = models.CharField(max_length=20, primary_key=True)

    def __unicode__(self):
        return self.orange_kind


class Expresskind(models.Model):
    expresskind = models.CharField(max_length=20, primary_key=True)

    def __unicode__(self):
        return self.expresskind


class Order(models.Model):
    order_num = models.CharField(max_length=20, primary_key=True)
    order_date = models.DateField()
    recieve_name = models.CharField(max_length=30)
    recieve_pthon = models.CharField(max_length=15)
    orange_kind = models.ForeignKey(OrangeKind)
    orange_weight = models.IntegerField()
    pay_name = models.CharField(max_length=30)
    express_name = models.ForeignKey(Expresskind)
    express_num = models.CharField(max_length=50)
    send_date = models.DateField()
    note = models.TextField()
    is_recieve = models.BooleanField(default=False)
    is_payed = models.BooleanField(default=False)
    recieve_date = models.DateField()

    def __unicode__(self):
        return self.order_num
