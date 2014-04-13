from django.shortcuts import render
from users.forms import RegisterForm,LoginForm
from django.http import HttpResponseRedirect
import string
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
import random
from users.models import TMSUser
def home(request):
    return render(request,'index.html',{})

def register(request):
    if request.user.is_authenticated():
	    return HttpResponseRedirect('/')
    url='/register'
    sub='Register'
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            em = form.cleaned_data['email']
            name = form.cleaned_data['name']
            contact = form.cleaned_data['contact']
            pwd = form.cleaned_data['password']
            uname = form.cleaned_data['username'] 
	    team = form.cleaned_data['team']
	    u = TMSUser.objects.filter(username=uname)
	    if u:
		    text = 'Username already exists'
            	    return render(request,'register.html',{'form':form,'url':url,'sub':sub,'text':text})
            u,created = TMSUser.objects.get_or_create(
                                        username=uname,
                                        first_name=name,
                                        email=em,
                                        contact=contact,
					team=team,
                                        )
            
            u.set_password(pwd)
            u.save()

            return HttpResponseRedirect('/')
        else:
            return render(request,'register.html',{'form':form,'url':url,'sub':sub})
    else:
        form=RegisterForm()
        return render(request,'register.html',{'form':form,'url':url,'sub':sub})

def logging(request):
    url='/login'
    sub='Login'
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            em = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            u = TMSUser.objects.filter(email=em)
            if not u:
                text = 'Email does not exist'
                return render(request,'message.html',{'text':text})
            u = u[0]
            user = authenticate(username=u.username,
                                password=pwd)
            if not user:
                text = "Password incorrect"
                return render(request,'register.html',{'text':text,'url':url,'sub':sub})
            if not user.is_active:
                text = 'Activate your account with the code sent to your mail id'
                return render(request,'message.html',{'text':text})
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            form = LoginForm()
            return render(request,'register.html',{'url':url,'form':form,'sub':sub})
    else:
        form = LoginForm()
        return render(request,'register.html',{'url':url,'form':form,'sub':sub})
        
def logoff(request):
    logout(request)
    return HttpResponseRedirect('/')

