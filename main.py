import json

def cadastrar_colaborador(): #Cadastro de Funcionários

    
    print("\n=== Cadastro de Colaborador ===")

    nome = input("Digite o nome do colaborador:")
    print("Colaborador Cadastrado:",nome)

    cargo = input("Digito o cargo do Colaborador:")
    print("Cargo Adicionado:", cargo)

    setor = input("Qual o setor?")
    print("Setor adicionado:", setor)

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


    try:
        with open("colaboradores.json","r") as arquivo:
            colaboradores = json.load(arquivo)

    except (FileNotFoundError, json.JSONDecodeError):
        colaboradores = []

    colaboradores.append(colaborador)

    with open("colaboradores.json","w") as arquivo:
        json.dump(colaboradores, arquivo, indent=4)

    print("\nColaborador salvo com sucesso!")
    input("\nPressione ENTER para voltar ao menu...")

def listar_colaboradores(): #Listar Colaboradores

    try:
      with open("colaboradores.json", "r") as arquivo:
          colaboradores = json.load(arquivo)

    except (FileNotFoundError, json.JSONDecodeError):
        colaboradores = []

    if not colaboradores:
        print("Lista Vazia")  
    else:
        for colaborador in colaboradores:
            print("Nome:", colaborador["nome"])
            print("Cargo:", colaborador["cargo"])
            print("Setor:", colaborador["setor"])
            print("Salário:", colaborador["salario"])
            print("----------------")

    input("\nPressione ENTER para voltar ao menu...")

def editar_colaborador(): #Editar colaboradores
    try:
        with open("colaboradores.json", "r") as arquivo:
            colaboradores = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        colaboradores = []

    if not colaboradores:
        print("Lista Vazia")
        return

    for indice, colaborador in enumerate(colaboradores):
        print(indice + 1, "-", colaborador["nome"])
    escolha = int(input("Escolha o colaborador a ser editado: "))

    colaborador = colaboradores[escolha-1]

    print("Nome:", colaborador["nome"])
    print("Cargo:", colaborador["cargo"])
    print("Setor:", colaborador["setor"])
    print("Salário:", colaborador["salario"])

    print("1 - Alterar nome")
    print("2 - Alterar cargo")
    print("3 - Alterar setor")
    print("4 - Alterar salário")

    opcao = input("O que deseja alterar?")

    if opcao == "1":
        colaborador["nome"] = input("Digite o novo nome: ")

    elif opcao == "2":
        colaborador["cargo"] = input("Digite o novo cargo: ")

    elif opcao == "3":
        colaborador["setor"] = input("Digite o novo setor: ")

    elif opcao == "4":
        colaborador["salario"] = float(input("Digite o novo salário: ").replace(",", "."))

    with open("colaboradores.json", "w") as arquivo:
        json.dump(colaboradores, arquivo, indent=4)

    print("Alterações Realizadas")
    
while True:  # Menu 

    print("=== Sistema de RH ===")
    print("1 - Cadastrar Funcionário")
    print("2 - Listar Funcionários")
    print("3 - Editar Lista")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Você escolheu cadastrar")
        cadastrar_colaborador()

    elif opcao == "2":
        print("Listando Funcionários")
        listar_colaboradores()

    elif opcao == "3":
        print("Editar Lista")   
        editar_colaborador() 

    elif opcao == "4":
        print("Sistema fechado")
        break