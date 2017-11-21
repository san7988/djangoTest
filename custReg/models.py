from django.db import models

class Customer(models.Model):
	custId = models.CharField(max_length=3)
	custName = models.CharField(max_length=200)
	custAge = models.CharField(max_length=2)