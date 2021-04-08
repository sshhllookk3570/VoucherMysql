from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import VoucherForm
from .models import Voucher
from django.views.generic import TemplateView
from django.shortcuts import render,HttpResponse,redirect
from Voucher.models import Voucher
from Consumer.forms import ConsumerForm


class Voucherview(TemplateView):
    template_name = 'voucher/voucher.html'

    def get(self,request):
        form = VoucherForm()
        return render(request, self.template_name, {'form': form})


    def post(self,request):
        form = VoucherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Voucher added")

        return render(request, self.template_name, {'form': form})


class Vouchershow(TemplateView):
    def post(self,request):
        voucher=Voucher.objects.all()
        n = []
        for i in voucher:
            n.append({'code': i.code,
                  'face_value': i.face_value,
                  'Start_date': i.start_date,
                  'expriy_date': i.expiry_date}
                 )

        return HttpResponse(n)




class Voucherassign(TemplateView):
    def get(self,request):
        form = ConsumerForm()
        return render(request, 'voucher/consumerform.html', {'form': form})

    def post(self,request):
        form = ConsumerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'voucher/stata.html', {'form': form})

        return render(request, 'voucher/status.html', {'form': form})




def index(request):
    return  render(request,'voucher/adminhome.html')

"""class get_data():
    template_name='voucher/voucher.html'

    def get(self,request):
        form=VoucherForm()
        return render(request,self.template_name, {'form': form})

    def post(self,request):
        form=VoucherForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=VoucherForm()
            code = form.cleaned_data('code')
            face_value = form.cleaned_data('face_value')
            start_date = form.cleaned_data('start_date')
            expiry_date = form.cleaned_data('expiry_date')
            form= VoucherForm()
            return  redirect('voucher:voucher')

        #args={'form':form,'code':code,'face_value':face_value,'start_date':start_date,'expiry_date':expiry_date}
        return render(request,self.template_name,{'form':form})"""
