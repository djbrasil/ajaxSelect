from django.urls import path

from . import views

urlpatterns = [
        #       path('', views.solicitacao_create_view, name='solicitacao_add'),
        #       path('<int:pk>/', views.solicitacao_update_view, name='solicitacao_change'), 
        #       path('ajax/load-solicitacao/', views.load_empresas, name='ajax_load_empresas'),
        path('', views.SolicitacaoListView.as_view(), name='home'), 
        path('solicitacao/', views.SolicitacaoNewView.as_view(), name='solicitacao-novo'), 
        
        path('ajax/load-solicitacao/', views.Load_empresas.as_view(), name='ajax_load_empresas'),
        path('sendmail/<str:pk>/', views.SolicitacaoCreate.as_view(), name='solicitacao-create'),
         
]