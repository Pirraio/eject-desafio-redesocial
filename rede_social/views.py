from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rede_social.models import Usuario, Postagem, Comentario
from rede_social.serializers import UsuarioSerializer, PostagemSerializer, ComentarioSerializer, ListaComentarioPostagemSerializer, ListaPostagemUsuarioSerializer, FeedPostagemSerializer
from django_filters.rest_framework import DjangoFilterBackend

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']

class PostagensViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['usuario__username', 'texto']
    ordering_fields = ['id', 'data_hora']
    ordering = ['-data_hora']
    serializer_class = PostagemSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['usuario__username', 'comentario']
    ordering_fields = ['id', 'data_hora']
    ordering = ['data_hora']
    serializer_class = ComentarioSerializer

class ListaPostagemUsuario(generics.ListAPIView):
    def get_queryset(self):
        queryset = Postagem.objects.filter(usuario_id = self.kwargs['pk'])
        return queryset
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['usuario__username', 'texto']
    ordering_fields = ['id', 'data_hora']
    ordering = ['-data_hora']
    serializer_class = ListaPostagemUsuarioSerializer

class ListaComentarioPostagem(generics.ListAPIView):
    def get_queryset(self):
        queryset = Comentario.objects.filter(postagem_id = self.kwargs['pk'])
        return queryset
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['usuario__username', 'comentario']
    ordering_fields = ['id', 'data_hora']
    ordering = ['data_hora']
    serializer_class = ListaComentarioPostagemSerializer

class FeedPostagem(generics.ListAPIView):
    queryset = Postagem.objects.all().order_by('-data_hora')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['usuario__username', 'texto']
    ordering_fields = ['id', 'data_hora']
    ordering = ['-data_hora']
    serializer_class = FeedPostagemSerializer