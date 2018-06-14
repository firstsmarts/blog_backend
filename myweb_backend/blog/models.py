# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=30)
    create_time = models.CharField(max_length=12)
    desc = models.CharField(max_length=50)
    author = models.CharField(max_length=20)




















