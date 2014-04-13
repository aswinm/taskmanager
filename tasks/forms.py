from django import forms

class AddListForm(forms.Form):
	name = forms.CharField(max_length=100)
