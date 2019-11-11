from django import forms
from .models import Processo

class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = ['nu_Processo', 'dt_Processo', 'ar_Processo', 'vl_Processo', 'cod_TipoProcesso', 'cod_Materia', 'cod_Forma']
