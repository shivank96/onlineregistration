from django.shortcuts import render,redirect
from django.contrib.messages.views import SuccessMessageMixin
from  django.views.generic import TemplateView,CreateView,ListView,UpdateView,DetailView,DeleteView,View


def Index(request):
    return render(request,"index.html")