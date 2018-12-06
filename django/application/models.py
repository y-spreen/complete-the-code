# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class LinkModel(models.Model):
    status = models.IntegerField(default=0)
    number = models.IntegerField()
