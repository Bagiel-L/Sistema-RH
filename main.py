import json

print("=== Sistema de RH ===")

nome = input("Digite o nome do colaborador:")
print("Colaborador Cadastrado",nome)

cargo = input("Digito o cargo do Colaborador:")
print("Cargo Adicionado", cargo)

setor = input("Qual o setor?")
print("Setor adicionado", setor)

salario = float(input("Digite o salário: ").replace(",", "."))
print("Salário cadastrado:",salario)

colaborador = {
    "nome": nome,
    "cargo": cargo,
    "setor": setor,
    "salario": salario
}

print("\n=== Colaborador Cadastrado ===")
print("Nome:", colaborador["nome"])
print("Cargo:", colaborador["cargo"])
print("Setor:", colaborador["setor"])
print("Salário:", colaborador["salario"])

with open("colaboradores.json","r") as arquivo:
    colaboradores = json.load(arquivo)

colaboradores.append(colaborador)

with open("colaboradores.json","w") as arquivo:
    json.dump(colaboradores, arquivo, indent=4)

    print("\nColaborador salvo com sucesso!")