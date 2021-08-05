from django.db import models


class AtributoChoices(models.TextChoices):
    FORCA = "forca", "Força"
    DESTREZA = "destreza", "Destreza"
    PRECISAO = "precisao", "Precisão"
    INTELIGENCIA = "inteligencia", "Inteligência"
    SABEDORIA = "sabedoria", "Sabedoria"
    CARISMA = "carisma", "Carisma"
    RESISTENCIA = "resistencia", "Resistência"
    FOCO = "foco", "Foco"
    ESQUIVA = "esquiva", "Esquiva"


class ElementoChoices(models.TextChoices):
    FOGO = "fogo", "Fogo"
    AGUA = "agua", "Água"
    TERRA = "terra", "Terra"
    AR = "ar", "Ar"
    VAZIO = "vazio", "Vazio"


class AlinhamentoChoices(models.TextChoices):
    LEAL_BOM = 'leal_bom', 'Leal e Bom'
    NEUTRO_BOM = 'neuto_bom', 'Neutro e Bom'
    CAOTICO_BOM = 'caotico_bom', 'Caótico e Bom'
    LEAL_NEUTRO = 'leal_neutro', 'Leal e Neutro'
    NEUTRO = 'neutro', 'Neutro'
    CAOTICO_NEUTRO = 'caotico_neutro', 'Caótico e Neutro'
    LEAL_MAU = 'leal_mau', 'Leal e Mau'
    NEUTRO_MAU = 'neutro_mau', 'Neutro e Mau'
    CAOTICO_MAU = 'caotico_mau', 'Caótico e Mau'
