from __future__ import unicode_literals

from django.db import models

from django.utils import timezone
# Create your models here.

class Answer(models.Model):

	key = models.CharField(max_length=200)
	author = models.ForeignKey('auth.User')
	question = models.TextField()
	content = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)
	upvotes = models.IntegerField()
	views = models.IntegerField()

	def __str__(self):
		return self.key
