from django.conf.urls import url,patterns
from tasks import views

urlpatterns = patterns('',
		url(r'^addlist/?$',views.AddList),
		url(r'^lists/(?P<teamname>\w+)/?$',views.displaylist),
		url(r'^addtask/?$',views.addtask),
		url(r'^mytasks/?',views.mytasks),
		url(r'^deletetask/(?P<tid>\d+)/?$',views.deletetask),
		url(r'^completetask/(?P<tid>\d+)/?$',views.completetask),
		url(r'^notifications/?$',views.notifications),
		)
