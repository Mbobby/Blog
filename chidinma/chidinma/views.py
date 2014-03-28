from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from chidinma.forms import MyRegistrationForm

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username = username, password = password)

	#check if login is valid and act appropriately

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/loggedin')
	else:
		return HttpResponseRedirect('/invalid')


def logout(request):
	auth.logout(request)
	return render_to_response("loggedout.html")

def loggedin(request):
	return render_to_response('loggedin.html', {"name": request.user.username})

def invalid(request):
	return render_to_response('invalid.html')

"""Methods to handle registration """

def register(request):
	if request.method == "POST":
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/register_success')


	c = {}
	c.update(csrf(request))
	c['form'] = MyRegistrationForm()
	return render_to_response('register.html', c)

def register_success(request):
	return render_to_response('register_success.html')
