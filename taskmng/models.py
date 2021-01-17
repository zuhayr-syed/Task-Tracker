from django.db import models

# Create your models here.

class Task(models.Model):
	title = models.CharField(max_length=200) # takes the name of the task
	complete = models.BooleanField(default=False) # set the default completed status to false for each item (not completed)
	created = models.DateTimeField(auto_now_add=True) # everytime model is created

	def __str__(self):
		return self.title # to return the task name to user