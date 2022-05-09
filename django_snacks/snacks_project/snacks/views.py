from re import template
from django.shortcuts import render
from django.views.generic import TemplateView


class BaseView(TemplateView):
    template_name='base.html'

class AboutView(TemplateView):
    template_name='about.html'

class HomeView(TemplateView):
    template_name='home.html'
