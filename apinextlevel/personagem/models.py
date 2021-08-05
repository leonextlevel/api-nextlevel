from django.db import models
from django.db.models.fields import PositiveSmallIntegerField

from .choices import AtributoChoices, ElementoChoices, AlinhamentoChoices


class Equipamento(models.Model):
    nome = models.CharField("Nome", max_length=100)
    descricao = models.TextField("Descrição")
    valor = PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.nome


class Pericia(models.Model):
    nome = models.CharField("Nome", max_length=100)
    atributo_base = models.CharField(
        "Atributo Base",
        max_length=15,
        choices=AtributoChoices.choices,
    )
    descricao = models.TextField("Descrição")

    def __str__(self) -> str:
        return self.nome


class Magia(models.Model):
    nome = models.CharField("Nome", max_length=100)
    elemento = models.CharField(
        "Elemento",
        max_length=15,
        choices=ElementoChoices.choices,
    )
    custo = models.PositiveSmallIntegerField("Custo")
    descricao = models.TextField("Descrição")

    def __str__(self) -> str:
        return self.nome


class Personagem(models.Model):

    # Básico
    nome = models.CharField("Nome", max_length=100)
    alinhamento = models.CharField(
        "Alinhamento",
        max_length=15,
        choices=AlinhamentoChoices.choices,
    )

    # Descrição
    altura = models.PositiveSmallIntegerField("Altura")
    idade = models.PositiveSmallIntegerField("Idade")
    cor_olho = models.CharField("Cor do olho", max_length=100)
    cor_cabelo = models.CharField("Cor do cabelo", max_length=100)
    cor_pele = models.CharField("Cor do pele", max_length=100)
    peso = models.PositiveSmallIntegerField("Peso")
    outras_caracteristicas = models.TextField("Outras Características")

    caracteristica_marcante = models.TextField("Característica Marcante")

    # Atributos Básicos
    max_hp = models.PositiveSmallIntegerField("HP Máximo")
    max_mp = models.PositiveSmallIntegerField("MP Máximo")

    # Atributos Principais
    forca = models.SmallIntegerField("Força")
    destreza = models.SmallIntegerField("Destreza")
    precisao = models.SmallIntegerField("Precisão")
    inteligencia = models.SmallIntegerField("Inteligência")
    sabedoria = models.SmallIntegerField("Sabedoria")
    carisma = models.SmallIntegerField("Carisma")
    resistencia = models.SmallIntegerField("Resistência")
    foco = models.SmallIntegerField("Foco")
    esquiva = models.SmallIntegerField("Esquiva")

    # Atributo Épico
    sorte = models.SmallIntegerField("Sorte")

    equipamentos = models.ManyToManyField(
        Equipamento,
        through="PersonagemEquipamento",
        through_fields=("personagem", "equipamento"),
        blank=True,
    )

    pericias = models.ManyToManyField(
        Pericia,
        through="PersonagemPericia",
        through_fields=("personagem", "pericia"),
        blank=True,
    )

    magias = models.ManyToManyField(
        Magia,
        through="PersonagemMagia",
        through_fields=("personagem", "magia"),
        blank=True,
    )

    class Meta:
        verbose_name = "Personagem"
        verbose_name_plural = "Personagens"

    def __str__(self) -> str:
        return self.nome


class PersonagemEquipamento(models.Model):

    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    quantidade = models.PositiveSmallIntegerField("Quantidade", default=1)

    class Meta:
        verbose_name = "Personagem Equipamento"
        verbose_name_plural = "Personagens Equipamentos"

    def __str__(self) -> str:
        return f'{self.equipamento} {self.personagem}'


class PersonagemPericia(models.Model):

    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE)
    pericia = models.ForeignKey(Pericia, on_delete=models.CASCADE)
    valor = models.PositiveSmallIntegerField("Valor", default=1)

    class Meta:
        verbose_name = "Personagem Pericia"
        verbose_name_plural = "Personagens Pericias"

    def __str__(self) -> str:
        return f'{self.pericia} {self.personagem}'


class PersonagemMagia(models.Model):

    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE)
    magia = models.ForeignKey(Magia, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Personagem Magia"
        verbose_name_plural = "Personagens Magias"

    def __str__(self) -> str:
        return f'{self.magia} {self.personagem}'
