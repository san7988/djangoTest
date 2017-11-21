# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	template = loader.get_template('custReg/index.html')
	context = dict()
	return HttpResponse(template.render(context, request))

def register(request):
	return render(request, 'custReg/register.html')

def search(request):
	return HttpResponse("In search method")

def populateData(request)
