from django.db import models

class Voucher(models.Model):
    code = models.CharField(max_length=15,unique=True)
    face_value=models.IntegerField()
    start_date=models.DateField()
    expiry_date=models.DateField()
