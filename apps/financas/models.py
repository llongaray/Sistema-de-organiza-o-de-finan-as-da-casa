from django.db import models
from django.contrib.auth.models import User
from django import forms

class Despesa(models.Model):
    TIPO_CHOICES = [
        ('CASA', 'Conta Casa'),
        ('MERC', 'Mercadinho'),
        ('LAZR', 'Lazer'),
        ('EXTR', 'Extra'),
    ]
    
    STATUS_CHOICES = [
        ('PAGO', 'Pago'),
        ('FIAD', 'Fiado'),
        ('APAG', 'À Pagar'),
        ('ANDA', 'Em Andamento'),
    ]
    
    data = models.DateField()
    tipo = models.CharField(max_length=4, choices=TIPO_CHOICES)
    descricao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'
        
    def __str__(self):
        return f"{self.get_tipo_display()} - R$ {self.valor}"

class Receita(models.Model):
    TIPO_CHOICES = [
        ('SALA', 'Salário'),
        ('DOAC', 'Doação'),
        ('EMPR', 'Emprestado'),
        ('EXTR', 'Extra'),
    ]
    
    STATUS_CHOICES = [
        ('RECB', 'Recebido'),
        ('AREC', 'À Receber'),
    ]
    
    data = models.DateField()
    tipo = models.CharField(max_length=4, choices=TIPO_CHOICES)
    descricao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        
    def __str__(self):
        return f"{self.get_tipo_display()} - R$ {self.valor}"

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
