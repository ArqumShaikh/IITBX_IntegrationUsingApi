from django.db import models

# Create your models here.
class repoclone(models.Model):
	url = models.TextField()
	directory = models.TextField()

	def __str__(self):
		return self.url
