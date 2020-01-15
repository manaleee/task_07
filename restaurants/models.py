from django.db import models

class Restaurant(models.Model):
    class Meta"
    	name = models.CharField(max_length=120)
    	description = models.TextField()
    	opening_time = models.TimeField()
    	closing_time = models.TimeField()
