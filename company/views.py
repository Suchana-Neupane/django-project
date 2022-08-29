from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Company

class CompanyBaseView(View):
    model = Company
    fields = '__all__'
    success_url = reverse_lazy('company:all')

class CompanyListView(CompanyBaseView, ListView):
    """View to list all company.
    Use the 'company_list' variable in the template
    to access all Company objects"""

class CompanyDetailView(CompanyBaseView, DetailView):
    """View to list the details from one company.
    Use the 'company' variable in the template to access
    the specific company here and in the Views below"""

class CompanyCreateView(CompanyBaseView, CreateView):
    """View to create a new company"""

class CompanyUpdateView(CompanyBaseView, UpdateView):
    """View to update a company"""

class CompanyDeleteView(CompanyBaseView, DeleteView):
    """View to delete a company"""