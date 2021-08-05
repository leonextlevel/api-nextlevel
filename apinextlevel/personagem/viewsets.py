from rest_framework import generics

from .models import Personagem
from .serializers import PersonagemSerializer


class PersonagemListAPIView(generics.ListAPIView):
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer


class PersonagemCreateAPIView(generics.CreateAPIView):
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer


class PersonagemUpdateAPIView(generics.UpdateAPIView):
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer


class PersonagemDestroyAPIView(generics.DestroyAPIView):
    queryset = Personagem.objects.all()
