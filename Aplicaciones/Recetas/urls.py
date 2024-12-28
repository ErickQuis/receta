from django.urls import path
from . import views
from .views import listado_receta
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio), 
    path('crear_receta/', views.crear_receta),
    path('listado_receta/', views.listado_receta, name='listado_receta'),
    path('listar_comentario/', views.listar_comentario, name='listar_comentario'),
    path('guardarreceta/', views.guardar_receta, name='guardar_receta'),
    path('editarreceta/<int:id>/', views.editarreceta, name='editarreceta'),
    path('eliminar_receta/<int:id>/', views.eliminar_receta, name='eliminar_receta'),
    path('tarjetas_recetas/', views.tarjetas_recetas, name='tarjetas_recetas'),
    path('detalle_receta/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),
    path('guardar_comentario/', views.guardar_comentario, name='guardar_comentario'),
    path('eliminar_comentario/<int:id>/', views.eliminar_comentario, name='eliminar_comentario'),

 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

