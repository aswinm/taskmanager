from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
	def __unicode__(self):
		return self.name
	tid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)

class TMSUser(User):
	team = models.ForeignKey(Team)
	contact = models.CharField(max_length=100,blank=True,null=True)
	


# Create your models here.
