from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm


# Login user
def login_user(request):
	if request.user.is_authenticated:
		return redirect(reverse('site:index'))

	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(
				request,
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password']
			)
			if user is not None:
				login(request, user)
				if 'next' in request.GET:
					return redirect(request.GET['next'])
				else:
					return redirect(reverse('news:admin_news_list'))
		else:
			form = LoginForm(request.POST)
	else:
		form = LoginForm()

	template = 'users/login_user.html'
	return render(request, template, {'form': form})


# Logout user
def logout_user(request):
	logout(request)
	return redirect(reverse('site:index'))