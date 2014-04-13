from django.db import models
from users.models import TMSUser

class List(models.Model):
	def __unicode__(self):
		return self.name
	lid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	creator = models.ForeignKey(TMSUser)

class Task(models.Model):
	def __unicode__(self):
		return self.name
	tid = models.AutoField(primary_key=True)
	Lis = models.ForeignKey(List)
	name = models.CharField(max_length=100)
	creator = models.ForeignKey(TMSUser,related_name='creator')
	assignedto = models.ForeignKey(TMSUser,related_name='assigned',blank=True,null=True,default=None)
	due_date = models.DateTimeField(blank=True,null=True)
	isSeen = models.BooleanField(default=False)
	isCompleted = models.BooleanField(default=False)

class Notification(models.Model):
	nid = models.AutoField(primary_key=True)
	content = models.CharField(max_length=100)
	url = models.CharField(max_length=100)
	isSeen = models.BooleanField(default=False)
	notify = models.ForeignKey(TMSUser,blank=True,null=True)



# Create your models here.
