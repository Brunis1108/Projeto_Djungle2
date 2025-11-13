from funcionario.models import Funcionarios

# # Criar e salvar um novo funcionário
# funcionarios = Funcionarios(
#     nome='Welison',
#     sobrenome='de Brito',
#     cpf='015.458.895-50',
#     tempo_de_servico=5,
#     remuneracao=1500.00
# )
# funcionarios.save()

# print("Funcionário salvo com sucesso:", funcionarios.nome, funcionarios.sobrenome)

funcionario = Funcionarios.objectos.get(id=2)

