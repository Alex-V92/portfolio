from django.db import models
from datetime import datetime

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default=None)
    date = models.DateField(default=datetime.now)