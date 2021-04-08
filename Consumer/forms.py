from django import  forms
from Consumer.models import Consumer

class ConsumerForm(forms.ModelForm):
    mobile = forms.IntegerField()
    code = forms.CharField(max_length=15)

    class Meta:
        model=Consumer
        fields=('mobile',
                'code',
                )

class ConsumervouchForm(forms.Form):
    mobile = forms.IntegerField()