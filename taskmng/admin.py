from django.contrib import admin

# Register your models here.

from .models import * # import all models (tasks)

admin.site.register(Task) # register to admin interface