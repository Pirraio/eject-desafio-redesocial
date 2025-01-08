from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rede_social.views import UsuarioViewSet, PostagensViewSet, ComentarioViewSet, ListaPostagemUsuario, ListaComentarioPostagem, FeedPostagem, CadastrarUsuario, CustomTokenObtainPairView, CustomTokenRefreshView


router = routers.DefaultRouter()
router.register('cadastrar', CadastrarUsuario, basename='Cadastrar')
router.register('usuarios', UsuarioViewSet, basename='Usuários')
router.register('postagens', PostagensViewSet, basename='Postagens')
router.register('comentarios', ComentarioViewSet, basename='Comentário')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('usuarios/<str:pk>/postagens/',ListaPostagemUsuario.as_view()),
    path('postagens/<str:pk>/comentarios/',ListaComentarioPostagem.as_view()),
    path('feed/',FeedPostagem.as_view()),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
