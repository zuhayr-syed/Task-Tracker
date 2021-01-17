from django.urls import path 
from . import views

urlpatterns = [ # function index from views.py
	path('', views.index, name="list"), #(when homepage is called, denoted with '')
	path('update_task/<str:pk>/', views.updateTask, name="update_task"), # path for updatedTask (creates unique url based on the pk(task's name))
	path('delete/<str:pk>/', views.deleteTask, name="delete"), # url path for deleting task
]