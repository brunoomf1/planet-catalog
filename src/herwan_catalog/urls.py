from django.urls import path
from herwan_catalog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novo_planeta/', views.novo_planeta, name='novo_planeta'),
    path('salvar_planeta/', views.salvar_planeta, name='salvar_planeta'),
]