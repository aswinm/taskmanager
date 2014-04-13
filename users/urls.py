from django.conf.urls import url,patterns
from users import views

urlpatterns = patterns('',
		url(r'^$',views.home),
		url(r'^register/?$',views.register),
		url(r'^login/?$',views.logging),
		url(r'^logout/?$',views.logoff),
		)
