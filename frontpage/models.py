from __future__ import unicode_literals

from django.db import models

from django.utils import timezone
# Create your models here.

class Question(models.Model):

	author = models.ForeignKey('auth.User')
	question = models.TextField()
	question_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.question

class Answer(models.Model):

	author = models.ForeignKey('auth.User')
	question = models.ForeignKey(Question)
	content = models.TextField()
	answer_date = models.DateTimeField(blank=True, null=True)
	
	def __str__(self):
		return self.question