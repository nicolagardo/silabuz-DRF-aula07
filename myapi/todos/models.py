from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(null= True)
    done_at = models.DateField(null=True)
    status = models.IntegerField(default=0)