# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import LinkModel
import random

def url_view(request):
    link = LinkModel.objects.filter(status=0).first()
    link.status = 1
    link.save()

    return HttpResponse(link.number)

def url_success_view(request, num, code):
    link = LinkModel.objects.get(number=num)

    if code == 404:
        link.delete()
    else:
        link.status = code
        link.save()

    return HttpResponse("")
