from django.contrib import admin
from django.urls import path
from Voucher.views import Voucherview,Vouchershow,Voucherassign
from Voucher import views

app_name = 'Voucher'
urlpatterns = [
    path("see/", Voucherview.as_view() ),
    path("", views.index,),
    path("show/",Vouchershow.as_view(),name='show'),
    path("assign/", Voucherassign.as_view(),name='assign'),


]
