from django.db import models
'''
#Caso precise relacionar com a tabela Usuario, criada na app usuarios
from apps.usuarios.models import Usuario


#Apagar a palavra pass e completar com os atributos da tabela
class Tipo_Evento(models.Model):
    pass


class Evento(models.Model):
    #demais atributos...
    tipo_evento = models.ForeignKey(Tipo_Evento, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)


class Tipo_Submissao(models.Model):
    pass


#Apagar a palavra pass e completar com os atributos da tabela
class Submissao(models.Model):
    #demais atributos...
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)
    tipo_submissao = models.ForeignKey(Tipo_Submissao, on_delete=models.PROTECT)
    
'''