from django.db import models

# Create your models here.

class Booklist(models.Model):
    isbn13 = models.CharField(max_length=150)
    title = models.TextField()
    image = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
