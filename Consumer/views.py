from django.shortcuts import render,redirect,HttpResponse
from .forms import ConsumervouchForm
from .models import Consumer
from Voucher.models import Voucher
from django.views.generic import TemplateView

class Consumerview(TemplateView):

    def get(self,request):
        form = ConsumervouchForm()
        return render(request, 'Consumer/vouchsearch.html', {'form': form})

    def post(self, request):

            form = ConsumervouchForm(request.POST)
            if form.is_valid():
                m=form.cleaned_data['mobile']
                #return HttpResponse(m)
                cod=Consumer.objects.filter(mobile=m)

                for i in cod:
                    vouch=Voucher.objects.filter(code=i.code)
                n=[]
                for i in vouch:
                    n.append({'code': i.code,
                              'face_value': i.face_value,
                              'Start_date': i.start_date,
                              'expriy_date': i.expiry_date}
                             )
                return HttpResponse(n)
            else:
                return render(request, 'Consumer/stata.html', {'form': form})

    #return render(request, 'Consumer/status.html', {'form': form})
