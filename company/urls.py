from django.urls import path
from . import views

app_name = 'companys'

urlpatterns = [
    path('', views.CompanyListView.as_view(), name='all'),
    path('companys/<int:pk>/detail', views.CompanyDetailView.as_view(), name='company_detail'),
    path('companys/create/', views.CompanyCreateView.as_view(), name='company_create'),
    path('companys/<int:pk>/update/', views.CompanyUpdateView.as_view(), name='company_update'),
    path('companys/<int:pk>/delete/', views.CompanyDeleteView.as_view(), name='company_delete'),
]