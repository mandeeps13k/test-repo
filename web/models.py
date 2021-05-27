# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ReferenceString(models.Model):
	reference_string = models.CharField(max_length = 255, verbose_name = "Reference String")
	akamai_response  = models.TextField(verbose_name = "Akamai Response") 

	def __unicode__(self):
		return self.reference_string
