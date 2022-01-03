from django.db import models

# Create your models here.
class book(models.Model):
    book_name=models.CharField(max_length=200)
    book_id=models.IntegerField(max_length=10)
    author=models.CharField(max_length=100)
