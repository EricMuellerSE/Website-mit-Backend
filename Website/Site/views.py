
# Views erstellen eine (Klasse) mit dem Jeweiligen Template und den benötigten daten welche in den URLs Abgerufen wird.


from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from .models import Kommentare
from .forms import KommentareForm
from .bw import badwords

# Home
def home(request):

  form = KommentareForm()
  if request.method == 'POST':
    form = KommentareForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("/home/")
  
  for i in Kommentare.objects.all():
      for badword in badwords:
        if badword in i.comment.lower() or badword in i.player.lower():
          i.delete()
          break


  comments = Kommentare.objects.all().values()
  template = loader.get_template('home.html')
  context= {
    'comments' : comments,
    'form' : form,
  }
  return HttpResponse(template.render(context, request))

# Was ist Airsoft
def wias(request):

  form = KommentareForm()
  if request.method == 'POST':
      form = KommentareForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect("/wias/")

  template = loader.get_template('wias.html')
  context= {
    'form' : form,
  }
  return HttpResponse(template.render(context, request))

# Gelände
def gelaende(request):

  form = KommentareForm()
  if request.method == 'POST':
      form = KommentareForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect("/gelaende/")

  template = loader.get_template('map.html')
  context= {
    'form' : form,
  }
  return HttpResponse(template.render(context, request))

# Downloads
def downloads(request):

  form = KommentareForm()
  if request.method == 'POST':
      form = KommentareForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect("/downloads/")

  template = loader.get_template('downloads.html')
  context= {
    'form' : form,
  }
  return HttpResponse(template.render(context, request))

# Kalender
def kalender(request):

  form = KommentareForm()
  if request.method == 'POST':
      form = KommentareForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect("/kalender/")

  template = loader.get_template('kalender.html')
  context= {
    'form' : form,
  }
  return HttpResponse(template.render(context, request))

# Interessiert?
def interessiert(request):

  form = KommentareForm()
  if request.method == 'POST':
      form = KommentareForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect("/interessiert/")

  template = loader.get_template('interessiert.html')
  context= {
    'form' : form,
  }
  return HttpResponse(template.render(context, request))

# Kontakt
def kontakt(request):

  form = KommentareForm()
  if request.method == 'POST':
      form = KommentareForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect("/kontakt/")

  template = loader.get_template('kontakt.html')
  context= {
    'form' : form,
  }
  return HttpResponse(template.render(context, request))

# Impressum
def impressum(request):

  form = KommentareForm()
  if request.method == 'POST':
      form = KommentareForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect("/impressum/")

  template = loader.get_template('impressum.html')
  context= {
    'form' : form,
  }
  return HttpResponse(template.render(context, request))

