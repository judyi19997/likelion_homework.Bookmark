from django.db import models

# Create your models here.

class bookmarkModel(models.Model):
    site_name = models.CharField(max_length = 20)
    site_url = models.CharField(max_length = 1000)

