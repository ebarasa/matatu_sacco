from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data('username')
			messages.success(request, f'Your Account has been Created! You are now able to Login')
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, 'users/register.html', {'form':'form'})


@login_required
def profile(request):
	return render(request, 'users/profile.html')

@login_required
def detail(request):
	return render(request, 'users/detail.html')

@login_required
def activity(request):
	return render(request, 'users/activity.html')

@login_required
def report(request):
	return render(request, 'users/report.html')