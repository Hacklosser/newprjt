import email
from sqlite3 import Time
from unicodedata import name
from django.db import models
from zmq import Message

# Create your models here.
class food (models.Model):
    name= models.TextField()
    email= models.EmailField()
    phone= models.IntegerField()
    Date= models.DateField()
    Time= models.TimeField()
    people= models.IntegerField()
    Message= models.TextField()