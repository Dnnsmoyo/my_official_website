# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Contact(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=75)
	phone = models.IntegerField(max_length=100)
	message = models.TextField()

	def __str__(self):
		return self.first_name