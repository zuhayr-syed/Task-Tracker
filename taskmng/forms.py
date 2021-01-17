# form representations of a model (creates form)
from django import forms
from django.forms import ModelForm

from .models import * # import all models

class TaskForm(forms.ModelForm):
	# widget grabs the form field and sets the defualt text input to placeholder text
	title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add New Task...'})) 

	class Meta: # the metaclass (inner class) defines how the class behaves (to provide metadata to the ModelForm class)
		model = Task # which model for form (model class to use for creating Form)
		fields = '__all__' # which fields allowed in form (list to fields to include in the Form)
						   # '__all__' indicates that all fields in the model should be used.