from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist 


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
	messages.add_message(request, messages.INFO, "Login failed!")
    return render_to_response('login.html', context_instance=RequestContext(request))

def register_user(request):
    logout(request) 
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']
        if password != password_repeat:
	    msg = "Password and Repeat Password fields not match."
        elif username and password and password_repeat:
            user = None
  	    msg = "User with the same username already exsists"
	    try:
	        check_username = User.objects.get(username=username)
	    except ObjectDoesNotExist:
	        check_username = None
	        user = User(username=username)
		user.set_password(password)
                user.is_staff = True
	        user.is_active = True
                user.save()
	        msg = "User - %s successfully created." % username
	    except Exception, e:
	        msg = e
            if user is not None:
	        new_user = authenticate(username=username, password=password)
		if new_user is not None and new_user.is_active:
		    print new_user, username, password
	            login(request, new_user)
	            return HttpResponseRedirect('/')
        else:
            msg = "Errors in the form"
	messages.add_message(request, messages.INFO, msg)
    return render_to_response('register.html', context_instance=RequestContext(request))

