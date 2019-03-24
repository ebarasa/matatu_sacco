from django.shortcuts import render
from .models import Comment


def home(request):
	context = {
		'comments': Comment.objects.all()
	}
	return render(request, 'sacco/home.html', context)

def about(request):
	return render(request, 'sacco/about.html', {'title':'About'})
def services(request):
	return render(request, 'sacco/services.html', {'title':'Services'})

def membership(request):
	return render(request, 'sacco/membership.html', {'title':'Membership'})

def infocenter(request):
	return render(request, 'sacco/infocenter.html', {'title':'InfoCenter'})

def csr(request):
	return render(request, 'sacco/csr.html', {'title':'CSR'})

def contacts(request):
	return render(request, 'sacco/contacts.html', {'title':'Contacts'})

def post(request):
	return render(request, 'sacco/post.html', {'title': 'Post'})

def announcements(request):
	return render(request, 'sacco/announcements.html', {'title': 'announcements'})

def events(request):
	return render(request, 'sacco/events.html', {'title': 'events'})

def calendars(request):
	return render(request, 'sacco/calendars.html', {'title': 'calendars'})

def complaints(request):
	return render(request, 'sacco/complaints.html', {'title': 'complaints'})

def messages(request):
	return render(request, 'sacco/messages.html', {'title': 'messages'})

def help(request):
	return render(request, 'sacco/help.html', {'title': 'help'})

def suggestions(request):
	return render(request, 'sacco/suggestions.html', {'title': 'suggestions'})

def etc(request):
	return render(request, 'sacco/etc.html', {'title': 'etc'})