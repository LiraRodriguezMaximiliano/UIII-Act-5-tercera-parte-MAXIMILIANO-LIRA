from django.urls import path
from . import views

urlpatterns = [
    # Inicio
    path('', views.inicio_Granja_Vacas, name='inicio'),

    # CRUD Vacas
    path('vacas/agregar/', views.agregar_vaca, name='agregar_vaca'),
    path('vacas/', views.ver_vacas, name='ver_vacas'),
    path('vacas/actualizar/<int:pk>/', views.actualizar_vaca, name='actualizar_vaca'),
    path('vacas/editar/<int:pk>/guardar/', views.realizar_actualizacion_vaca, name='realizar_actualizacion_vaca'),
    path('vacas/borrar/<int:pk>/', views.borrar_vaca, name='borrar_vaca'),

    # CRUD Producción 🥛
    path('produccion/', views.ver_produccion, name='ver_produccion'),
    path('produccion/agregar/', views.agregar_produccion, name='agregar_produccion'),
    path('produccion/actualizar/<int:pk>/', views.actualizar_produccion, name='actualizar_produccion'),
    path('produccion/editar/<int:pk>/guardar/', views.realizar_actualizacion_produccion, name='realizar_actualizacion_produccion'),
    path('produccion/borrar/<int:pk>/', views.borrar_produccion, name='borrar_produccion'),
    # CRUD Evento Sanitario
    path('evento/', views.ver_evento_sanitario, name='ver_evento_sanitario'),
    path('evento/agregar/', views.agregar_evento_sanitario, name='agregar_evento_sanitario'),
    path('evento/actualizar/<int:pk>/', views.actualizar_evento_sanitario, name='actualizar_evento_sanitario'),
    path('evento/editar/<int:pk>/guardar/', views.realizar_actualizacion_evento_sanitario, name='realizar_actualizacion_evento_sanitario'),
    path('evento/borrar/<int:pk>/', views.borrar_evento_sanitario, name='borrar_evento_sanitario'),

]

