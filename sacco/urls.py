from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sacco-home'),
    path('about/', views.about, name='sacco-about'),
    path('services/', views.services, name='sacco-services'),
    path('membership/', views.membership, name='sacco-membership'),
    path('infocenter/', views.infocenter, name='sacco-infocenter'),
    path('csr/', views.csr, name='sacco-csr'),
    path('contacts/', views.contacts, name='sacco-contacts'),
]