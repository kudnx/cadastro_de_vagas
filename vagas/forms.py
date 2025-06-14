from django import forms


class VagaForm(forms.Form):
    nome_da_vaga = forms.CharField()
    nome_da_empresa = forms.CharField()
    link_da_vaga = forms.CharField()
    descricao_da_vaga = forms.CharField(required=False)
    responsavel_pela_vaga = forms.CharField(required=False)
    detalhes = forms.CharField(required=False)
    observacoes = forms.CharField(required=False)
