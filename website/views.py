from django.shortcuts import render, get_object_or_404, redirect
from funcionario.models import Funcionarios

# Create your views here.


def index(request):
    return render(request, 'website/index.html')

def listar_funcionarios(request):
    funcionarios = Funcionarios.objetos.all().order_by('id')
    contexto = {"funcionarios": funcionarios}
    return render(request, 'website/index.html', contexto)

def detalhes_funcionario(request, id):
    funcionario = get_object_or_404(Funcionarios, pk=id)
    contexto = {"funcionario": funcionario}
    return render(request, 'website/detalhesFuncionario.html', contexto)

# def cadastrar_funcionario(request):
#     funcionarios = Funcionarios.objetos.all()
#     contexto = {"funcionario": funcionario}
#     return render(request, 'website/detalhesFuncionario.html', contexto)

def editar_funcionario(request, id):
    if request.method == "POST":
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        cpf = request.POST.get("cpf")
        tempo_de_serviço = request.POST.get("tempo_de_serviço")
        remuneracao = request.POST.get("remuneracao")
        
        funcionario = Funcionarios(
            nome =nome
            sobrenome =sobrenome
            cpf = cpf
            tempo_de_serviço = tempo_de_serviço
            remuneracao = remuneracao
        )
        funcionario.save()
    return redirect("website:index", id=funcionario.id)

    return render(request, 'website/detalhesFuncionario.html', contexto)


def excluir_funcionario(request, id):
    funcionario = get_object_or_404(Funcionarios, pk=id)
    # Exclusão imediata sem confirmação:
    funcionario.delete()
    return redirect('website:listar')

# def excluir_funcionario(request, id):
#     funcionario = get_object_or_404(Funcionarios, pk=id)
#     if request.method == "POST":
#         funcionario.delete()
#         return redirect('website:listar')  # ou o nome de rota que lista
#     contexto = {"funcionario": funcionario}
#     return render(request, 'website/confirmar_excluir.html', contexto)