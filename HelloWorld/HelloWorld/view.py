# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context          = {}
    context['hello'] = 'Hello World!!!'
    context['hi'] = 'HI!'
    return render(request, 'student_home.html', context)