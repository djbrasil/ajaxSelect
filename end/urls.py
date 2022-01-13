from django.urls import path

from . import views

urlpatterns = [
    path('', views.solicitacao_create_view, name='solicitacao_add'),
    path('<int:pk>/', views.solicitacao_update_view, name='solicitacao_change'), 
    path('ajax/load-solicitacao/', views.load_empresas, name='ajax_load_empresas'),
]