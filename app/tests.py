from django.test import TestCase
from django.urls import reverse

from app.models import Aluno


class AlunoCrudTests(TestCase):

    def setUp(self):
        self.aluno = Aluno.objects.create(nome='Ana Souza', matricula='2025001')

    def test_lista_mostra_alunos(self):
        resposta = self.client.get(reverse('lista_alunos'))
        self.assertContains(resposta, 'Ana Souza')

    def test_busca_por_nome(self):
        Aluno.objects.create(nome='Bruno Lima', matricula='2025002')
        resposta = self.client.get(reverse('lista_alunos'), {'q': 'bruno'})
        self.assertContains(resposta, 'Bruno Lima')
        self.assertNotContains(resposta, 'Ana Souza')

    def test_cadastrar_aluno(self):
        resposta = self.client.post(reverse('novo_alunos'), {'nome': 'Carla Dias', 'matricula': '2025003'})
        self.assertRedirects(resposta, reverse('lista_alunos'))
        self.assertTrue(Aluno.objects.filter(matricula='2025003').exists())

    def test_matricula_repetida_nao_cadastra(self):
        resposta = self.client.post(reverse('novo_alunos'), {'nome': 'Outra Pessoa', 'matricula': '2025001'})
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Já existe um aluno com essa matrícula.')
        self.assertEqual(Aluno.objects.count(), 1)

    def test_matricula_com_letras_nao_cadastra(self):
        self.client.post(reverse('novo_alunos'), {'nome': 'Teste', 'matricula': 'abc123'})
        self.assertEqual(Aluno.objects.count(), 1)

    def test_editar_aluno(self):
        url = reverse('atualizar_alunos', args=[self.aluno.id])
        self.assertContains(self.client.get(url), '2025001')  # formulário já vem preenchido
        self.client.post(url, {'nome': 'Ana Souza Lima', 'matricula': '2025001'})
        self.aluno.refresh_from_db()
        self.assertEqual(self.aluno.nome, 'Ana Souza Lima')

    def test_excluir_aluno(self):
        resposta = self.client.post(reverse('deletar_alunos', args=[self.aluno.id]))
        self.assertRedirects(resposta, reverse('lista_alunos'))
        self.assertFalse(Aluno.objects.exists())

    def test_excluir_por_get_nao_funciona(self):
        resposta = self.client.get(reverse('deletar_alunos', args=[self.aluno.id]))
        self.assertEqual(resposta.status_code, 405)
        self.assertTrue(Aluno.objects.exists())
