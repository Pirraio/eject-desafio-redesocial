from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rede_social.models import Usuario, Postagem, Comentario
from rede_social.serializers import UsuarioSerializer, PostagemSerializer, ComentarioSerializer, ListaComentarioPostagemSerializer, ListaPostagemUsuarioSerializer, FeedPostagemSerializer, CadastrarUsuarioSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class CadastrarUsuario(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    serializer_class = CadastrarUsuarioSerializer
    http_method_names = ['post']

class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']

class PostagensViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Postagem.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['usuario__username', 'texto']
    ordering_fields = ['id', 'data_hora']
    ordering = ['-data_hora']
    serializer_class = PostagemSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class ComentarioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comentario.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['usuario__username', 'comentario']
    ordering_fields = ['id', 'data_hora']
    ordering = ['data_hora']
    serializer_class = ComentarioSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class ListaPostagemUsuario(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Postagem.objects.filter(usuario_id = self.kwargs['pk'])
        return queryset
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['usuario__username', 'texto']
    ordering_fields = ['id', 'data_hora']
    ordering = ['-data_hora']
    serializer_class = ListaPostagemUsuarioSerializer

class ListaComentarioPostagem(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Comentario.objects.filter(postagem_id = self.kwargs['pk'])
        return queryset
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['usuario__username', 'comentario']
    ordering_fields = ['id', 'data_hora']
    ordering = ['data_hora']
    serializer_class = ListaComentarioPostagemSerializer

class FeedPostagem(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Postagem.objects.all().order_by('-data_hora')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['usuario__username', 'texto']
    ordering_fields = ['id', 'data_hora']
    ordering = ['-data_hora']
    serializer_class = FeedPostagemSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            tokens = response.data

            access_token = tokens['access']
            refresh_token = tokens['refresh']
            username = request.data['username']

            try:
                user = Usuario.objects.get(username=username)
            except Usuario.DoesNotExist:
                return Response({'error':'usuario não existe'})

            res = Response()

            res.data = {"success":True,
                        "user": {
                            "username":user.username,
                            "email":user.email,
                            "name": user.name,
                            }
                        }
            res.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )
            res.set_cookie(
                key='refresh_token',
                value=refresh_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )
            return res

        except:
            return Response({'success':False})

class CustomTokenRefreshView(TokenRefreshView):
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            request.data['refresh'] = refresh_token
            response = super().post(request, *args, **kwargs)
            
            tokens = response.data
            access_token = tokens['access']
            res = Response()
            res.data = {'sucess': True}

            res.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )

            return res

        except Exception as e:
            print(e)
            return Response({'sucess': False})
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        res = Response()
        res.data = {'success':True}
        res.delete_cookie('access_token', path='/', samesite='None')
        res.delete_cookie('response_token', path='/', samesite='None')
        
        return res
    except Exception as e:
        print(e)
        return Response({'success':False})