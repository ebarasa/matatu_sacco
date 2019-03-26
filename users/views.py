from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, OwnerUpdateForm
from .models import Owner, Matatu, Activity_log, Crew, Finance

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Account has been Created! You are now able to Login')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your Account has been Updated!')
			return redirect('profile')			

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form,
	}
	return render(request, 'users/profile.html', context)


@login_required
def detail(request):
	# import pdb; pdb.set_trace();
	context = {
		'owners' : Owner.objects.filter(user_id=request.user.id),
	}
	return render(request, 'users/detail.html', context)

@login_required
def activity(request):
	owner_id = 0
	owner = Owner.objects.filter(user_id=request.user.id)
	if len(owner) > 0:
		owner_id = owner[0].id
	matatus = Matatu.objects.filter(owner_id=owner_id)
	matatu_ids = list(map(lambda x: x.id, matatus))
	context = {
		'activity_logs': Activity_log.objects.filter(pk__in=matatu_ids).order_by('-Date_Time_of_record'),
	}
	return render(request, 'users/activity.html', context)

@login_required
def matatu(request):
	owner_id = 0
	owner = Owner.objects.filter(user_id=request.user.id)
	if len(owner) > 0:
		owner_id = owner[0].id
	context = {
		'matatus' : Matatu.objects.select_related('owner').filter(owner_id=owner_id),
	}
	return render(request, 'users/matatu.html', context)

@login_required
def crew(request, matatu_id):
	context = {
		'crews' : Crew.objects.filter(matatu_id=matatu_id),
		'matatu': Matatu.objects.get(id=matatu_id)
	}
	return render(request, 'users/crew.html', context)

@login_required
def finance(request, matatu_id):
	finances = Finance.objects.filter(matatu_id=matatu_id).order_by('-date_time')
	total_income = 0
	total_exp = 0
	for fin in finances:
		if fin.finance_type == 'income':
			total_income += fin.amount
		else:
			total_exp += fin.amount

	context = {
		'finances' : finances,
		'matatu': Matatu.objects.get(id=matatu_id),
		'total_income': total_income,
		'total_exp': total_exp,
		'net_income': total_income - total_exp
	}

	return render(request, 'users/finance.html', context)

