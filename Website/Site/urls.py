
# URLs sind dafür zuständig die richtigen views für die jeweilige URL Abfrage zu Laden

from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home, name='home'),
    path('wias/', views.wias, name='wias'),
    path('gelaende/', views.gelaende, name='gelaende'),
    path('downloads/', views.downloads, name='downloads'),
    path('kalender/', views.kalender, name='kalender'),
    path('interessiert/', views.interessiert, name='interessiert'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('impressum/', views.impressum, name='impressum'),
]
