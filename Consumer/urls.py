from django.contrib import admin
from django.urls import path
from Consumer.views import Consumerview

urlpatterns = [
    path("",  Consumerview.as_view()),


]
