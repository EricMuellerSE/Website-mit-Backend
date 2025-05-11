# Forms erstellen Automatisch generierte Formulare welche dann mit Variablen in die Templates eingefügt werden können.

from django import forms
from .models import Kommentare
from django.forms import ModelForm, TextInput, EmailInput

class KommentareForm(forms.ModelForm):
    class Meta:
        model = Kommentare
        fields = ('player', 'comment')
        widgets = {
            'player': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Spielername',
                'text': 'Spielername',
                'style': 'margin-bottom : 20px; border-color: var(--bs-body-color); width: 95%; margin-left: 2.5%;',
                }),
            'comment': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Kommentar',
                'style' : 'margin-bottom : 20px; border-color: var(--bs-body-color); width: 95%; margin-left: 2.5%;',
                })
        }
        labels = {
            'player': 'Spielername',
            'comment': 'Kommentar',
        }