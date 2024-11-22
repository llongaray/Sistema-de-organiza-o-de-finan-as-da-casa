from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DespesaForm, ReceitaForm
from .models import Despesa, Receita
from django.contrib.auth.models import User
from datetime import datetime, timedelta

@login_required
def dashboard(request):
    # Obter todos os usuários para o filtro
    usuarios = User.objects.all()

    # Definir o mês atual
    hoje = datetime.now()
    primeiro_dia = hoje.replace(day=1)
    ultimo_dia = (primeiro_dia + timedelta(days=31)).replace(day=1) - timedelta(days=1)

    # Inicializar as variáveis de filtro
    data_inicio = request.GET.get('data_inicio', primeiro_dia.strftime('%Y-%m-%d'))
    data_fim = request.GET.get('data_fim', ultimo_dia.strftime('%Y-%m-%d'))
    usuario_id = request.GET.get('usuario')

    # Filtrar despesas e receitas com base nos filtros
    despesas = Despesa.objects.filter(usuario=request.user).order_by('-data')
    receitas = Receita.objects.filter(usuario=request.user).order_by('-data')

    if data_inicio and data_fim:
        despesas = despesas.filter(data__range=[data_inicio, data_fim])
        receitas = receitas.filter(data__range=[data_inicio, data_fim])

    if usuario_id:
        despesas = despesas.filter(usuario_id=usuario_id)
        receitas = receitas.filter(usuario_id=usuario_id)

    total_despesas = sum(despesa.valor for despesa in despesas)
    total_receitas = sum(receita.valor for receita in receitas)
    saldo = total_receitas - total_despesas

    context = {
        'title': 'Dashboard Financeiro',
        'description': 'Visão geral das suas finanças',
        'despesas': despesas,
        'receitas': receitas,
        'total_despesas': total_despesas,
        'total_receitas': total_receitas,
        'saldo': saldo,
        'usuarios': usuarios,  # Passar a lista de usuários para o template
        'data_inicio': data_inicio,
        'data_fim': data_fim,
        'usuario_id': usuario_id,
    }
    return render(request, 'financas/dashboard.html', context)

@login_required
def nova_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.usuario = request.user
            despesa.save()
            messages.success(request, 'Despesa registrada com sucesso!')
            return redirect('financas:dashboard')
    else:
        form = DespesaForm()
    
    context = {
        'title': 'Nova Despesa',
        'form': form
    }
    return render(request, 'financas/form_despesa.html', context)

@login_required
def nova_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            receita = form.save(commit=False)
            receita.usuario = request.user
            receita.save()
            messages.success(request, 'Receita registrada com sucesso!')
            return redirect('financas:dashboard')
    else:
        form = ReceitaForm()
    
    context = {
        'title': 'Nova Receita',
        'form': form
    }
    return render(request, 'financas/form_receita.html', context)

@login_required
def list_receitas(request):
    if request.method == 'POST' and request.POST.get('form_type') == 'delete':
        pk = request.POST.get('receita_id')  # Obtém o ID da receita a ser deletada
        receita = Receita.objects.get(pk=pk, usuario=request.user)
        receita.delete()
        messages.success(request, 'Receita deletada com sucesso!')

        return redirect('financas:list_receitas')  # Redireciona para a lista de receitas

    receitas = Receita.objects.filter(usuario=request.user).order_by('-data')
    total_receitas = receitas.count()  # Contar o total de receitas

    context = {
        'title': 'Listar Receitas',
        'receitas': receitas,
        'total_receitas': total_receitas,
    }
    return render(request, 'financas/list_receitas.html', context)

@login_required
def list_despesas(request):
    if request.method == 'POST' and request.POST.get('form_type') == 'delete':
        pk = request.POST.get('despesa_id')  # Obtém o ID da despesa a ser deletada
        despesa = Despesa.objects.get(pk=pk, usuario=request.user)
        despesa.delete()
        messages.success(request, 'Despesa deletada com sucesso!')

        return redirect('financas:list_despesas')  # Redireciona para a lista de despesas

    despesas = Despesa.objects.filter(usuario=request.user).order_by('-data')
    total_despesas = despesas.count()  # Contar o total de despesas

    context = {
        'title': 'Listar Despesas',
        'despesas': despesas,
        'total_despesas': total_despesas,
    }
    return render(request, 'financas/list_despesas.html', context)

@login_required
def editar_receita(request, pk):
    receita = Receita.objects.get(pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=receita)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receita atualizada com sucesso!')
            return redirect('financas:list_receitas')
    else:
        form = ReceitaForm(instance=receita)
    
    context = {
        'title': 'Editar Receita',
        'form': form
    }
    return render(request, 'financas/form_receita.html', context)

@login_required
def editar_despesa(request, pk):
    despesa = Despesa.objects.get(pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = DespesaForm(request.POST, instance=despesa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Despesa atualizada com sucesso!')
            return redirect('financas:list_despesas')
    else:
        form = DespesaForm(instance=despesa)
    
    context = {
        'title': 'Editar Despesa',
        'form': form
    }
    return render(request, 'financas/form_despesa.html', context)

