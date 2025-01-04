from django.contrib import admin
from rede_social.models import Usuario, Postagem, Comentario

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'name', 'email']
    list_display_links = ['id', 'username']
    list_per_page = 30
    search_fields = ('username','email',)
    ordering = ('id',)

admin.site.register(Usuario, UsuariosAdmin)

class PostagensAdmin(admin.ModelAdmin):
    list_display = ['id', 'texto', 'data_hora']
    list_display_links = ['id']
    search_fields = ('texto',)

admin.site.register(Postagem,PostagensAdmin)

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'postagem', 'comentario', 'data_hora']
    list_display_links = ['id', 'usuario', 'postagem']
    search_fields = ('usuario', 'postagem', 'comentario',)
    
admin.site.register(Comentario,ComentariosAdmin)