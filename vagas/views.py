from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action

from .forms import VagaForm
from .models import Vaga
from .serializers import VagaSerializer

class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer

    @action(methods=['get'], detail=True)
    def detalhes(self, request, pk=None):
        return HttpResponse("You're looking at question %s." % pk)


def home(request):
    lista_de_vagas = Vaga.objects.all().order_by('-created_at')[:10]

    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            nome_da_vaga = form.cleaned_data['nome_da_vaga']
            nome_da_empresa = form.cleaned_data['nome_da_empresa']
            link_da_vaga = form.cleaned_data['link_da_vaga']
            descricao_da_vaga = form.cleaned_data['descricao_da_vaga'] if form.cleaned_data['descricao_da_vaga'] else ""
            responsavel_pela_vaga = form.cleaned_data['responsavel_pela_vaga'] if form.cleaned_data['responsavel_pela_vaga'] else ""
            detalhes = form.cleaned_data['detalhes'] if form.cleaned_data['detalhes'] else ""
            observacoes = form.cleaned_data['observacoes'] if form.cleaned_data['observacoes'] else ""

            houve_resposta = False

            # Save to database
            salvar_vaga = Vaga(
                nome_da_vaga=nome_da_vaga,
                nome_da_empresa=nome_da_empresa,
                link_da_vaga=link_da_vaga,
                houve_resposta=houve_resposta,
                descricao_da_vaga=descricao_da_vaga,
                responsavel_pela_vaga=responsavel_pela_vaga,
                detalhes=detalhes,
                observacoes=observacoes,
                )

            salvar_vaga.save()

            form = VagaForm()
            return render(request, 'home.html', {'form': form, 'lista_de_vagas': lista_de_vagas})
    else:
        form = VagaForm()

    return render(request, 'home.html', {'form': form, 'lista_de_vagas': lista_de_vagas})