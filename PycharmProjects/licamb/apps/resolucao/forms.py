from django import forms
from django.forms import ModelForm

from .models import (
    Divisao,
    Grupo,
)

class DivisaoForm(ModelForm):
    class Meta:
        model = Divisao
        fields = ['id', 'codigo', 'descricao']

class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = ['id', 'Divisao', 'descricao']