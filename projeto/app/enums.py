from django.db import models


class Status(models.TextChoices):
    FAZER   = 'FAZER',   'Fazer'
    FAZENDO = 'FAZENDO', 'Fazendo'
    PRONTO  = 'PRONTO',  'Pronto'


class Prioridade(models.TextChoices):
    BAIXA = 'BAIXA', 'Baixa'
    MEDIA = 'MEDIA', 'Média'
    ALTA  = 'ALTA',  'Alta'