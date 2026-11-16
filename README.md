# Cadastro de Alunos (Django)

CRUD simples de alunos feito em Django. Foi o projeto que usei para aprender o framework do zero: models, views, templates, formulários e o admin.

Dá pra cadastrar, listar, buscar, editar e excluir alunos. Cada aluno tem nome e matrícula, e a matrícula não pode se repetir.

## Tecnologias

- Python e Django 5.2
- SQLite
- Bootstrap 5 e Font Awesome no front

## Como rodar

```bash
git clone https://github.com/Rafael-Ramalho-code/projeto-django-alunos-CRUD.git
cd projeto-django-alunos-CRUD

python -m venv venv
source venv/bin/activate      # no Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Abra http://127.0.0.1:8000 e pronto.

Para entrar no admin do Django (`/admin`), crie um usuário antes com `python manage.py createsuperuser`.

## Testes

```bash
python manage.py test
```

Os testes cobrem cadastro, edição, exclusão, busca e os casos de erro (matrícula repetida ou com letras).

## Estrutura

```
config/      configurações e rotas principais
app/
  models.py  model Aluno
  forms.py   formulário com as validações de nome e matrícula
  views.py   listar, cadastrar, editar e excluir
  tests.py
templates/   base.html, lista.html e aluno_forms.html
```

## Rotas

| URL | O que faz |
|---|---|
| `/aluno/` | Lista os alunos (aceita `?q=` para buscar) |
| `/aluno/novo/` | Cadastra um aluno |
| `/aluno/<id>/` | Edita um aluno |
| `/aluno/<id>/delete/` | Exclui (só via POST, com confirmação na tela) |
