from django import forms
from .models import Question, Answer


#http://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth

class AskQuestion(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['question']

class PostAnswer(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['content']