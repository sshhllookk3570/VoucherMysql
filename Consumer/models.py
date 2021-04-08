from django.db import models
#from Voucher.models import Voucher

class Consumer(models.Model):
     mobile = models.IntegerField()
     code = models.CharField(max_length=15)
