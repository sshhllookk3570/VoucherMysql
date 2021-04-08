from django.shortcuts import render,HttpResponse
from .forms import MerchantForm
from Voucher.models import Voucher
from Consumer.models import Consumer
from django.views.generic import TemplateView

class Merchantview(TemplateView):

    def get(self,request):
        form = MerchantForm()
        return render(request, 'Merchant/Merchantredeem.html', {'form': form})

    def post(self, request):

            form = MerchantForm(request.POST)
            if form.is_valid():
                cod=form.cleaned_data['code']
                m=Consumer.objects.get(code=cod).mobile
                vouch=Voucher.objects.get(code=cod)
                n=[]
                n.append({'code': vouch.code,
                              'face_value': vouch.face_value,
                              'Start_date': vouch.start_date,
                              'expriy_date': vouch.expiry_date,
                              'mobile':m,
                          }
                             )
                return HttpResponse(n)
            else:
                return render(request, 'Merchant/stata.html', {'form': form})

