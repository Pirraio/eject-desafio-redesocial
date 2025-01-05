from rest_framework import serializers
from rede_social.models import Usuario, Postagem, Comentario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password', 'name', 'foto_perfil', 'data_criacao', 'data_nascimento']

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class ListaPostagemUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        exclude = ['usuario']

class ListaComentarioPostagemSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.username')
    class Meta:
        model = Comentario
        fields = ['usuario', 'comentario', 'data_hora']
