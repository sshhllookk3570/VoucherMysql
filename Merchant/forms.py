from django import  forms


class MerchantForm(forms.Form):
    code = forms.CharField()