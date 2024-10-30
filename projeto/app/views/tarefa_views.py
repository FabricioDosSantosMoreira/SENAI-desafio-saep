from datetime import datetime

import pytz
from app.forms import TarefaForm
from app.models import Tarefa
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .base import home

def cadastrar_tarefa(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = TarefaForm()

    context = {'form': form}

    return render(request, 'tarefas/cadastrar_tarefa.html', context=context)


def atualizar_tarefa(request: WSGIRequest, id: int) -> HttpResponse:
    tarefa: Tarefa = get_object_or_404(Tarefa, id=id)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()  
            return redirect(gerenciar_tarefas)
        
    else:
        form = TarefaForm(instance=tarefa)

    context = {'form': form, 'tarefa': tarefa}

    return render(request, 'tarefas/atualizar_tarefa.html', context=context)


def deletar_tarefa(request: WSGIRequest, id: int) -> HttpResponse:
    tarefa: Tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()

    return redirect(gerenciar_tarefas)


def gerenciar_tarefas(request: WSGIRequest) -> HttpResponse:
    tarefas: list[Tarefa] = Tarefa.objects.all()

    tarefas_fazer: list[Tarefa] = []
    tarefas_fazendo: list[Tarefa] = []
    tarefas_pronto: list[Tarefa] = []
    for tarefa in tarefas:
        # Formata a 'data_cadastro'
        tarefa.data_cadastro = tarefa.data_cadastro.astimezone(pytz.timezone('America/Sao_Paulo'))
        tarefa.data_cadastro = datetime.strftime(tarefa.data_cadastro, "%d/%m/%Y, %H:%M:%S")

        # Insere cada tarefa em sua lista
        if tarefa.status == 'FAZER':
            tarefas_fazer.append(tarefa)
        elif tarefa.status == 'FAZENDO':
            tarefas_fazendo.append(tarefa)
        elif tarefa.status == 'PRONTO':
            tarefas_pronto.append(tarefa)


    context = {
        'tarefas_fazer': tarefas_fazer,
        'tarefas_fazendo': tarefas_fazendo,
        'tarefas_pronto': tarefas_pronto
    }
    
    return render(request, 'tarefas/gerenciar_tarefas.html', context)


def atualizar_status_tarefa(request: WSGIRequest, id: int) -> HttpResponse:
    tarefa: Tarefa = get_object_or_404(Tarefa, id=id)
    
    novo_status = request.POST.get('status')

    if novo_status in ['FAZER', 'FAZENDO', 'PRONTO']:
        tarefa.status = novo_status
        tarefa.save()

    return redirect(gerenciar_tarefas)
