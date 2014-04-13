from django.contrib import admin
from users.models import TMSUser,Team

class UserAdmin(admin.ModelAdmin):
		pass

class TeamAdmin(admin.ModelAdmin):
	pass

admin.site.register(TMSUser,UserAdmin)
admin.site.register(Team,TeamAdmin)

# Register your models here.
