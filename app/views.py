from io import BytesIO

from django.http.multipartparser import MultiPartParser
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods

from app.models import Aluno

def lista_alunos(request):
    alunos = Aluno.objects.order_by('-criado_em')
    contexto = {'alunos': alunos,}
    return render(request,'lista.html', contexto)

@require_http_methods(['GET'])
def novo_alunos(request):
    return render(request, 'novo_aluno.html')

@require_http_methods(['POST'])
def cadastrar_alunos(request):
    nome = request.POST.get('nome')
    matricula = request.POST.get('matricula')

    if nome and matricula:
        Aluno.objects.create(nome=nome, matricula=matricula)
        return redirect('lista_alunos')

    contexto = {'error': 'Preencha o nome e o preço corretamente'}
    return render(request, 'novo_aluno.html', contexto)

@require_http_methods(['GET', 'PUT'])
def atualizar_alunos(request, id,):
    try:
        aluno = Aluno.objects.get(id=id)
    except Aluno.DoesNotExist:
        return redirect('lista_alunos')

    if request.method == 'GET':
        contexto = {'aluno': aluno,}
        return render(request, 'aluno_forms.html', contexto)

    stream = BytesIO(request.body)
    parser = MultiPartParser(request.META, stream, request.upload_handlers, request.encoding)

    data, files = parser.parse()

    nome = data.get('nome').strip()
    matricula = data.get('matricula').strip()

    if nome and matricula:
        try:
            aluno.nome = nome
            aluno.matricula = matricula
            aluno.save()
            return redirect('lista_alunos')
        except Aluno.DoesNotExist:
            contexto = {
                'aluno': aluno,
                'erro': 'Ocorreu um erro ao salvar. Tente novamente.'
            }
            return render(request, 'aluno_forms.html', contexto)

    contexto = {
        'aluno': aluno,
        'erro': 'Preencha nome e preço corretamente.'
    }
    return render(request, 'aluno_forms.html', contexto)

@require_http_methods(['DELETE'])
def deletar_alunos(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    contexto = { 'mensagem': 'Excluído com sucesso.' }
    return render(request, 'lista.html', contexto)

