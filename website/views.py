from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from funcionario.models import Funcionarios

def index(request):
    q = request.GET.get('q', '')
    funcionarios = Funcionarios.objetos.all().order_by('id')
    if q:
        funcionarios = funcionarios.filter(
            Q(nome__icontains=q) |
            Q(sobrenome__icontains=q) |
            Q(cpf__icontains=q)
        )
    contexto = {
        "titulo": "Funcionários de Bruna",
        "funcionarios": funcionarios,
        "q": q,
        "total": funcionarios.count()
    }
    return render(request, 'website/index.html', contexto)


def listar_funcionarios(request):
    return index(request)


def detalhes_funcionario(request, id):
    f = get_object_or_404(Funcionarios, pk=id)
    return render(request, 'website/detalhesFuncionario.html', {
        "titulo": f"Detalhes | {f.nome} {f.sobrenome}",
        "f": f
    })

# FORM para criar/editar
def _salvar_form(request, instancia=None):
    # Manualmente porque você ainda não tem um ModelForm neste app
    if request.method == "POST":
        data = request.POST
        campos = ("nome", "sobrenome", "cpf", "tempo_de_servico", "remuneracao")
        valores = {k: data.get(k) for k in campos}

        if instancia is None:
            instancia = Funcionarios(**valores)
            messages.success(request, "Funcionário cadastrado com sucesso!")
        else:
            for k, v in valores.items():
                setattr(instancia, k, v)
            messages.success(request, "Funcionário atualizado com sucesso!")

        instancia.save()
        return redirect('website:detalhes', id=instancia.id)

    return render(request, 'website/form_funcionario.html', {
        "titulo": "Novo Funcionário" if instancia is None else f"Editar | {instancia.nome} {instancia.sobrenome}",
        "f": instancia,
        "modo": "cadastrar" if instancia is None else "editar"
    })

def cadastrar_funcionario(request):
    return _salvar_form(request, None)

def editar_funcionario(request, id):
    f = get_object_or_404(Funcionarios, pk=id)
    return _salvar_form(request, f)

# EXCLUIR com confirmação
def excluir_funcionario(request, id):
    f = get_object_or_404(Funcionarios, pk=id)
    if request.method == "POST":
        f.delete()
        messages.warning(request, "Funcionário excluído.")
        return redirect('website:index')
    return render(request, 'website/confirmar_excluir.html', {"titulo": f"Excluir | {f.nome} {f.sobrenome}", "f": f})
