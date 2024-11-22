from django import forms
from .models import Despesa, Receita

class DespesaForm(forms.ModelForm):
    data = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    class Meta:
        model = Despesa
        fields = ['data', 'tipo', 'descricao', 'valor', 'status']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class ReceitaForm(forms.ModelForm):
    data = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    class Meta:
        model = Receita
        fields = ['data', 'tipo', 'descricao', 'valor', 'status']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }