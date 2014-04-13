from django.shortcuts import render
from tasks.models import List,Task
from django.contrib.auth.decorators import login_required
from tasks.forms import AddListForm
from users.models import TMSUser,Team
from django.http import HttpResponseRedirect

@login_required(login_url='/login')
def AddList(request):
	url='/addlist'
	sub='Add'
	u = TMSUser.objects.get(username=request.user.username)
	if request.method=="POST":
		form = AddListForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			l = List.objects.create(
				name=name,
				creator = u,
				)
			l.save()
			x = u.team.name
			x = x.lower()
			return HttpResponseRedirect('/lists/'+x)
		else:
			return render(request,'register.html',{'form':form,'sub':sub,'url':url})
	else:
		form = AddListForm()
		return render(request,'register.html',{'form':form,'sub':sub,'url':url})


@login_required(login_url='/login')
def displaylist(request,teamname):
	t = Team.objects.filter(name__icontains=teamname)
	print teamname
	if not t:
		return render(request,'404.html',{})
	t = t[0]
	lists = List.objects.filter(creator__team=t)
	q = None
	if lists:
		q = Task.objects.filter(Lis=lists[0]) 
		for i in lists:
			x = Task.objects.filter(Lis=i)
			q = q | x
		print q
	u = TMSUser.objects.get(username=request.user.username)
	if u.team==t:
		editable=True
	else:
		editable=False
	assigns = TMSUser.objects.filter(team__name=teamname)
	return render(request,'lists.html',{'lists':lists,'tasks':q,'editable':editable,'assigns':assigns})

@login_required(login_url='/login')
def addtask(request):
	u = TMSUser.objects.get(username=request.user.username)
	if request.method=="POST":
		name = request.POST['name']
		lis = request.POST['listname']
		l = List.objects.filter(lid=lis)
		if not l:
			return HttpResponseRedirect('/lists/'+u.team.name.lower())
		l = l[0]
		if l.creator.team.name != u.team.name:
			return HttpResponseRedirect('/lists/'+u.team.name.lower())
		t = Task.objects.create(
				name=name,
				creator = u,
				Lis = l,
				)
		t.save()
		x = u.team.name
		x = x.lower()
		return HttpResponseRedirect('/lists/'+x)
	else:
		return render(request,'404.html',{})

@login_required(login_url='/login')
def mytasks(request):
	u = TMSUser.objects.get(username=request.user.username)
	return HttpResponseRedirect('/lists/'+u.team.name.lower())


		
		


# Create your views here.
