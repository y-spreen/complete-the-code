from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import LinkModel
import random

def url_view(request):
    links = LinkModel.objects.filter(status__lt=2)
    links = [l for l in links]
    link = random.choice(links)

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
