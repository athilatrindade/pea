from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('atleta/', include('atleta.urls')),
    path('avaliacaoAtletismo/', include('avaliaAtletismo.urls')), 
    path('consulta/', include('consulta.urls')),
    path('instrutor/', include('instrutor.urls')),
    path('modalidade/', include('modalidade.urls')),
    path('teste/', include('teste.urls')),
    path('usuario/', include('usuario.urls')),
    path('dashboard/', include('dashboard.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

