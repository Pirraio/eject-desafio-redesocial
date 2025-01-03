from django.contrib import admin
from rede_social.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'name', 'email']
    list_display_links = ['id', 'username']
    list_per_page = 30
    search_fields = ('username','email',)
    ordering = ('id',)

admin.site.register(Usuario, UsuarioAdmin)
