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