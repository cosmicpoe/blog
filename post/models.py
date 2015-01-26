from django.db import models
from datetime import datetime
from django.utils import timezone


class Post(models.Model):
	title = models.CharField(max_length=128, unique=True)
	description = models.TextField()
	#date = models.DateField(_("Date"), default=datetime.date.today)
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

class Category(models.Model):
	posts = models.ManyToManyField(Post)
	name = models.CharField(max_length=128, unique=True)


	def __unicode__(self):
		return self.name
