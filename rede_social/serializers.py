from rest_framework import serializers
from rede_social.models import Usuario, Postagem, Comentario
from rest_framework.response import Response

class CadastrarUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'name',  'foto_perfil', 'data_nascimento']

    def create(self, validated_data):
        user = Usuario(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
            foto_perfil=validated_data['foto_perfil'],
            data_nascimento=validated_data['data_nascimento'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
class UsuarioSerializer(serializers.ModelSerializer): 
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    class Meta:
        model = Usuario
        fields = ['email', 'password', 'name', 'foto_perfil', 'data_criacao', 'data_nascimento']
    
    def update(self, user, validated_data):
        try:
            #user.username = validated_data.get('username', user.username)
            user.email = validated_data.get('email', user.email)
            user.name = validated_data.get('name', user.name)
            user.set_password(validated_data.get('password'))
            user.save()
            return user
        except:
            return Response({'sucess': False})

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = '__all__'
        read_only_fields = ("usuario",)

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
        read_only_fields = ("usuario",)

class ListaPostagemUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        exclude = ['usuario']

class ListaComentarioPostagemSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.username')
    class Meta:
        model = Comentario
        fields = ['usuario', 'comentario', 'data_hora']

class FeedPostagemSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.username')
    class Meta:
        model = Postagem
        fields = '__all__'