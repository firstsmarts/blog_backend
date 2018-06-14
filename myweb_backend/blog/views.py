# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.http import HttpResponse

from .models import Articles
import json
# Create your views here.


def getlist(request):
    res = {
        "status": 0,
        "data": list(Articles.objects.all().values('id', 'title', 'desc', 'create_time', 'author'))
    }
    return HttpResponse(json.dumps(res), 'application/json')


def api404(request):
    return HttpResponse('sorry')

