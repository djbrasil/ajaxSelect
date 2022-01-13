from django.urls import path

from . import views

urlpatterns = [
        #       path('', views.solicitacao_create_view, name='solicitacao_add'),
        #       path('<int:pk>/', views.solicitacao_update_view, name='solicitacao_change'), 
        #       path('ajax/load-solicitacao/', views.load_empresas, name='ajax_load_empresas'),
        
        path('ajax/load-solicitacao/', views.Load_empresas.as_view(), name='ajax_load_empresas'),
        path('', views.SolicitacaoCreate.as_view(), name='solicitacao-create'),   
        path('<int:pk>/', views.SolicitacaoUpdate.as_view(), name='solicitacao-update'),
]