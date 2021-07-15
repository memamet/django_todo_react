from django.db import models

# Create your models here.
<<<<<<< HEAD
=======

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
>>>>>>> 13e1ee0 (finished tutorial)
