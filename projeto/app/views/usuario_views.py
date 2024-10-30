from app.forms import UsuarioForm
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .base import home

def cadastrar_usuario(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = UsuarioForm()

    context = {'form': form}

    return render(request, 'usuarios/cadastrar_usuario.html', context=context)
