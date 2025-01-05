from django.shortcuts import render
from rest_framework import viewsets, generics
from rede_social.models import Usuario, Postagem, Comentario
from rede_social.serializers import UsuarioSerializer, PostagemSerializer, ComentarioSerializer, ListaComentarioPostagemSerializer, ListaPostagemUsuarioSerializer
from rest_framework import filters

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']

class PostagensViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class ListaPostagemUsuario(generics.ListAPIView):
    def get_queryset(self):
        queryset = Postagem.objects.filter(usuario_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaPostagemUsuarioSerializer

class ListaComentarioPostagem(generics.ListAPIView):
    def get_queryset(self):
        queryset = Comentario.objects.filter(postagem_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaComentarioPostagemSerializer