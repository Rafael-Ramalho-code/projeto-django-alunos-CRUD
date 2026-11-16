from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST

from app.forms import AlunoForm
from app.models import Aluno


def lista_alunos(request):
    busca = request.GET.get('q', '').strip()
    alunos = Aluno.objects.order_by('-criado_em')
    if busca:
        # filtra por parte do nome ou da matrícula
        alunos = alunos.filter(nome__icontains=busca) | alunos.filter(matricula__icontains=busca)
    return render(request, 'lista.html', {'alunos': alunos, 'busca': busca})


@require_http_methods(['GET', 'POST'])
def novo_alunos(request):
    form = AlunoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        aluno = form.save()
        messages.success(request, f'Aluno {aluno.nome} cadastrado.')
        return redirect('lista_alunos')
    return render(request, 'aluno_forms.html', {'form': form})


@require_http_methods(['GET', 'POST'])
def atualizar_alunos(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    form = AlunoForm(request.POST or None, instance=aluno)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Dados do aluno atualizados.')
        return redirect('lista_alunos')
    return render(request, 'aluno_forms.html', {'form': form, 'aluno': aluno})


@require_POST
def deletar_alunos(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    messages.success(request, f'Aluno {aluno.nome} excluído.')
    return redirect('lista_alunos')
