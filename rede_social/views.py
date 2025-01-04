from django.shortcuts import render
from rest_framework import viewsets
from rede_social.models import Usuario, Postagem, Comentario
from rede_social.serializers import UsuarioSerializer, PostagemSerializer, ComentarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PostagensViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer