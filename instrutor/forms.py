from django import forms
from . models import Instrutor, PerfilInstrutor

class CadastroInstrutor(forms.ModelForm):
    perfil = forms.ModelChoiceField(queryset=PerfilInstrutor.objects.all())

    class Meta:
        model = PerfilInstrutor
        fields = ['perfil']
        
