from django.db import models

class Vaga(models.Model):
    RESPOSTA = [
        ('nao_selecionado', 'não selecionado'),
        ('1_fase', '1 fase'),
        ('2_fase', '2 fase'),
        ('3_fase', '3 fase'),
        ('4_fase', '4 fase'),
        ('5_fase', '5 fase'),
        ('proposta', 'proposta'),
    ]

    nome_da_vaga = models.CharField()
    nome_da_empresa = models.CharField()
    data_da_canditatura = models.DateTimeField(auto_now_add=True)
    link_da_vaga = models.CharField()
    houve_resposta = models.BooleanField()
    resposta_final = models.CharField(
        max_length=50,
        choices=RESPOSTA,
        blank=True,
        null=True
    )
    descricao_da_vaga = models.CharField()
    responsavel_pela_vaga = models.CharField()
    detalhes = models.CharField()
    observacoes = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
