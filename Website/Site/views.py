from django.template import loader
from django.http import HttpResponse
from .models import Kommentare

def home(request):
  comments = Kommentare.objects.all().values()
  template = loader.get_template('home.html')
  context= {
    'comments' : comments,
  }
  return HttpResponse(template.render(context, request))

def wias(request):
  template = loader.get_template('wias.html')
  return HttpResponse(template.render())

def gelaende(request):
  template = loader.get_template('map.html')
  return HttpResponse(template.render())

def downloads(request):
  template = loader.get_template('downloads.html')
  return HttpResponse(template.render())

def kalender(request):
  template = loader.get_template('kalender.html')
  return HttpResponse(template.render())

def interessiert(request):
  template = loader.get_template('interessiert.html')
  return HttpResponse(template.render())

def kontakt(request):
  template = loader.get_template('kontakt.html')
  return HttpResponse(template.render())

def impressum(request):
  template = loader.get_template('Home.html')
  return HttpResponse(template.render())

