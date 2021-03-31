from django.shortcuts import render
from TestApp.models import Company
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class companylistview(ListView):
    model = Company
class companydetailview(DetailView):
    model = Company
class companycreateview(CreateView):
    model = Company
    fields ='__all__'
class companyupdateview(UpdateView):
    model = Company
    fields = ('Name','ceo')
class companydeleteview(DeleteView):
    model = Company
    success_url = reverse_lazy('company')
