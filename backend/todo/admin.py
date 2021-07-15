from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Todo, TodoAdmin)
>>>>>>> 13e1ee0 (finished tutorial)
