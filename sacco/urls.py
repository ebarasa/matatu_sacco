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
    path('post/', views.post, name='sacco-post'),
    path('announcements/', views.announcements, name='sacco-announcements'),
    path('events/', views.events, name='sacco-events'),
    path('calendars/', views.calendars, name='sacco-calendars'),
    path('complaints/', views.complaints, name='sacco-complaints'),
    path('messages/', views.messages, name='sacco-messages'),
    path('help/', views.help, name='sacco-help'),
    path('suggestions/', views.suggestions, name='sacco-suggestions'),
    path('etc/', views.etc, name='sacco-etc'),
    path('awards/', views.awards, name='sacco-awards'),
]