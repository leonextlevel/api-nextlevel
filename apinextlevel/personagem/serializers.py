from collections import OrderedDict

from django.db import transaction

from rest_framework import serializers

from .models import Personagem, Equipamento, Pericia, Magia


class EquipamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipamento
        fields = [
            'id',
            'nome',
            'valor',
            'descricao',
        ]


class PericiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pericia
        fields = [
            'id',
            'nome',
            'atributo_base',
            'descricao',
        ]


class MagiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Magia
        fields = [
            'id',
            'nome',
            'elemento',
            'descricao',
            'custo',
        ]


class PersonagemSerializer(serializers.ModelSerializer):

    equipamentos = serializers.PrimaryKeyRelatedField(
        queryset=Equipamento.objects.all(),
        many=True, required=False
    )
    pericias = serializers.PrimaryKeyRelatedField(
        queryset=Pericia.objects.all(),
        many=True, required=False
    )
    magias = serializers.PrimaryKeyRelatedField(
        queryset=Magia.objects.all(),
        many=True, required=False
    )

    class Meta:
        model = Personagem
        fields = [
            'id',
            'nome',
            'alinhamento',
            'altura',
            'idade',
            'cor_olho',
            'cor_cabelo',
            'cor_pele',
            'peso',
            'outras_caracteristicas',
            'caracteristica_marcante',
            'max_hp',
            'max_mp',
            'forca',
            'destreza',
            'precisao',
            'inteligencia',
            'sabedoria',
            'carisma',
            'resistencia',
            'foco',
            'esquiva',
            'sorte',
            'equipamentos',
            'pericias',
            'magias',
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['equipamentos'] = instance.equipamentos.values()
        ret['pericias'] = instance.pericias.values()
        ret['magias'] = instance.magias.values()
        return ret
