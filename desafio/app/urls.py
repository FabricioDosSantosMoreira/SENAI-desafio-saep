from django.urls import path

from app import views

urlpatterns = [
    path('', views.home, name='home'),

    path('usuarios/cadastrar', views.cadastrar_usuario,  name='cadastrar_usuario'),

    path('tarefas/cadastrar', views.cadastrar_tarefa, name='cadastrar_tarefa'),
    path('tarefas/atualizar/<int:id>', views.atualizar_tarefa, name='atualizar_tarefa'),
    path('tarefas/deletar/<int:id>', views.deletar_tarefa, name='deletar_tarefa'),
    path('tarefas/gerenciar', views.gerenciar_tarefas, name='gerenciar_tarefas'),
    path('tarefas/atualizar_status/<int:id>', views.atualizar_status_tarefa, name='atualizar_status_tarefa')
]
