from django import forms
from django.forms import ModelForm
from .models import comments,post


class commentform(forms.ModelForm):
	content=forms.CharField(widget=forms.Textarea(attrs={
		'class':'form-control',
		'placeholder':'Type your comment here',
		'id':'comment',
		'label':'Comment Area'

		}))
	class Meta:
		model=comments
		fields=['content']

class create_post_form(forms.ModelForm):
	class Meta:
		model=post
		fields=['title','overview','thumb_nail','categories']

	
	