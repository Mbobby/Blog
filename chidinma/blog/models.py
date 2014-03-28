from django.db import models
from time import time
from datetime import datetime

def get_file_name(instance, filename):
	return 'uploads/%s_%s' % (str(time()).replace('.', '_'), filename)


# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField(default = 0)
	thumbnail = models.FileField(upload_to = get_file_name)


	def __unicode__(self):
		return self.title

class Comment(models.Model):
	name = models.CharField(max_length = 200)
	body = models.TextField()
	pub_date = models.DateTimeField('Date published', default= datetime.now() )
	article = models.ForeignKey(Article)

	def __unicode__(self):
		return self.name

class Bio(models.Model):
	biography = models.TextField()
	date_modified = models.DateTimeField('date modified')

	def __unicode__(self):
		return "Biography!"

