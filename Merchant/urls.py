from django.contrib import admin
from django.urls import path
from Merchant.views import Merchantview

urlpatterns = [
    path("",Merchantview.as_view() ),


]
