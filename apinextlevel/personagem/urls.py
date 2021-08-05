from django.urls import path

from .viewsets import (
    PersonagemListAPIView,
    PersonagemCreateAPIView,
    PersonagemUpdateAPIView,
    PersonagemDestroyAPIView,
)

urlpatterns = [
    path('list/', PersonagemListAPIView.as_view(), name='personagem_list'),
    path('create/', PersonagemCreateAPIView.as_view(), name='personagem_create'),
    path('update/<int:pk>/', PersonagemUpdateAPIView.as_view(), name='personagem_update'),
    path('delete/<int:pk>/', PersonagemDestroyAPIView.as_view(), name='personagem_delete'),
]
