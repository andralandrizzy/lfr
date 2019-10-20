from django.db import models
from datetime import datetime
# Create your models here.


class Client(models.Model):
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    client_link = models.URLField(max_length=100, blank=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)
