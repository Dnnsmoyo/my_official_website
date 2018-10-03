# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import CreateView
# Create your views here.
class IndexView(CreateView):
	template_name='index.html'
	form_class = ContactForm
	success_url = '/'