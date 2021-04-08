from django import  forms
from Voucher.models import Voucher

class VoucherForm(forms.ModelForm):
    code = forms.CharField(max_length=15)
    face_value = forms.IntegerField()
    start_date = forms.DateField()
    expiry_date = forms.DateField()
    class Meta:
        model=Voucher
        fields=('code',
                'face_value',
                'start_date',
                'expiry_date',)