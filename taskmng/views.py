from django.shortcuts import render, redirect 
# redirect --> gives the HttpResponseRedirect for the argument passed (sends another request to the given url)
# render --> combines given template with given context dictionary and returns an HttpResponse object with that rendered text(request a page and the render function returns it)
from django.http import HttpResponse

from .models import * # import all models
from .forms import * # import all forms

# Create your views here.

def index(request): # make test function
	taskmng = Task.objects.all() # make a query for the imported models (grabbing the objects from class)

	form = TaskForm()

	if request.method =='POST': # for user input
		form = TaskForm(request.POST) # pass the POST method
		if form.is_valid(): # if user input is valid
			form.save() # saves information to database
		return redirect('/') # redirects back to form template (back to same url path)

	context = {'taskmng':taskmng, 'form':form} # make context dictionary to throw in all models directly into render function (to pass from model into template -html)
	return render(request, 'taskmng/list.html', context) # returns the template created (requesting a page and render returns it)

def updateTask(request, pk): # create new view with dynamic url path for updating item (also includes primary key)
	task = Task.objects.get(id=pk) # grabs object's id from the url pattern (pk) (to retrieve object)

	form = TaskForm(instance=task) # create form of an instance of the object selected (creates new form with prefilled information based on previous instance) 

	if request.method == 'POST': # if user inputs updated information
		form = TaskForm(request.POST, instance=task) # call on the previous instance, so that a new item is not created (only updating)
		if form.is_valid(): # if input is valid
			form.save() # save task information
			return redirect('/') #redirects back to homepage

	context = {'form':form} # create context for the updated form (dictionary with variable name as the key and their values as the value)

	return render(request, 'taskmng/update_task.html', context) #update render with context argument

def deleteTask(request, pk): # delete function
	item = Task.objects.get(id=pk) # using primary key to grab the specific task

	if request.method == 'POST': # if user selects delete
		item.delete() # deletes selected item
		return redirect('/') #redirects back to homepage


	context = {'item':item} # render context ()
	return render(request, 'taskmng/delete.html', context)