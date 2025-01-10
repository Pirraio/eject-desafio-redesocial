from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rede_social.views import UsuarioViewSet, PostagensViewSet, ComentarioViewSet, ListaPostagemUsuario, ListaComentarioPostagem, FeedPostagem, CadastrarUsuario, CustomTokenObtainPairView, CustomTokenRefreshView, logout
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('cadastrar', CadastrarUsuario, basename='Cadastrar')
router.register('usuarios', UsuarioViewSet, basename='Usuários')
router.register('postagens', PostagensViewSet, basename='Postagens')
router.register('comentarios', ComentarioViewSet, basename='Comentário')

schema_view = get_schema_view(
   openapi.Info(
      title="Documentação da API",
      default_version='v1',
      description="Informação sobre o que a API pode fazer, seus endpoints, etc",
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('usuarios/<str:pk>/postagens/',ListaPostagemUsuario.as_view()),
    path('postagens/<int:pk>/comentarios/',ListaComentarioPostagem.as_view()),
    path('feed/',FeedPostagem.as_view()),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', logout),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
