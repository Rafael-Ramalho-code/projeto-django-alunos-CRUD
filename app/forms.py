from django import forms

from app.models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'matricula']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Maria Silva', 'autofocus': True}),
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 20250012345', 'inputmode': 'numeric'}),
        }
        error_messages = {
            'matricula': {'unique': 'Já existe um aluno com essa matrícula.'},
        }

    def clean_nome(self):
        nome = self.cleaned_data['nome'].strip()
        if not nome:
            raise forms.ValidationError('Informe o nome do aluno.')
        return nome

    def clean_matricula(self):
        # matrícula só com números (aceita zeros à esquerda, por isso é texto e não int)
        matricula = self.cleaned_data['matricula'].strip()
        if not matricula.isdigit():
            raise forms.ValidationError('A matrícula deve conter apenas números.')
        return matricula
