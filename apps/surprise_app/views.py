# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random

values = ['Holy Toledo!', 'WHAT IS HAPPENING IN OAKLAND, RAY FOSSE?!', 'I HAVE NO IDEA, GLEN KUIPER!', 'They are walkin off again!', 'Other things!!', 'Supercalifragilisticexpialidocious', 'HotDog!', 'Appearing Ninja!', 'Disappearing Ninja', ]

# Create your views here.
def index(request):
	return render(request, 'surprise_app/index.html')

def submit(request):
	surprises = []
	if request.method == "POST":
		loop = 0
		for i in range(int(request.POST['count'])):
			randnum = random.randint(0, len(values)-1)
			surprises += [values[randnum]]
		request.session['list'] = surprises

	return redirect('/results')

def results(request):
	context = {
		'list': request.session['list']
	}
	return render(request, 'surprise_app/results.html', context)
