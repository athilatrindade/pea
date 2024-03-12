from django import forms
from . models import Instrutor, Usuario

class CadastroUsuario(forms.ModelForm):
    perfil = forms.ModelChoiceField(queryset=Instrutor.objects.all())

    class Meta:
        model = Instrutor
        fields = ['nome']
        
