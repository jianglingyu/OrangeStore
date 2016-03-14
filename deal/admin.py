from django.contrib import admin
from deal.models import OrangeKind,Expresskind,Order,user

admin.site.register(OrangeKind)
admin.site.register(Expresskind)
admin.site.register(Order)
admin.site.register(user)

# Register your models here.
