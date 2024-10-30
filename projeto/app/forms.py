from django import forms

from app.models import Tarefa, Usuario


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['nome', 'email']


class TarefaForm(forms.ModelForm):

    class Meta:
        model = Tarefa
        fields = ['usuario', 'descricao', 'nome_setor', 'prioridade']
