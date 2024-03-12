from django import forms
from . models import Atleta, Modalidade

class CadastroAtleta(forms.ModelForm):
    modalidade_atleta = forms.ModelChoiceField(queryset=Modalidade.objects.all())

    class Meta:
        model = Atleta
        fields = ['modalidade_atleta']
        
