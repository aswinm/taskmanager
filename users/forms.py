from django import forms
from users.models import Team

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=32)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    contact = forms.CharField(max_length=25,required=False)
    team = forms.ModelChoiceField(queryset=Team.objects.all())
    password = forms.CharField(max_length=32,widget=forms.PasswordInput())
    confirmPassword = forms.CharField(max_length=32,widget=forms.PasswordInput())
    
    
class LoginForm(forms.Form):
    email =  forms.EmailField()
    password = forms.CharField(max_length=32,widget=forms.PasswordInput())
    
