from django.db import models
from django.utils import timezone


# Create your models here.

class create_list(models.Model):
	namel = models.CharField(max_length=500)
	userl = models.CharField(max_length=100)
	datecl = models.DateField(default=timezone.now())
	dateml = models.DateField(blank=True, null=True)
