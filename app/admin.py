from django.contrib import admin
from app.models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'criado_em')
    search_fields = ('nome', 'matricula')
    list_filter = ('criado_em',)
