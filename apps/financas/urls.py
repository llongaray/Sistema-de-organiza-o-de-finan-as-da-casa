from django.urls import path
from .views import *

app_name = 'financas'

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("nova-despesa/", nova_despesa, name="nova_despesa"),
    path("nova-receita/", nova_receita, name="nova_receita"),
    path("listar-receitas/", list_receitas, name="list_receitas"),
    path("listar-despesas/", list_despesas, name="list_despesas"),
    path("editar-receita/<int:pk>/", editar_receita, name="editar_receita"),
    path("editar-despesa/<int:pk>/", editar_despesa, name="editar_despesa"),
]
