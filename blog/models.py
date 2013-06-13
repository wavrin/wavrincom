from django.db import models
from django.db.models import permalink

class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=100, unique=True)
	text = models.TextField()
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_post', None, {'slug': self.slug})