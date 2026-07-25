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

    except FileNotFoundError:
        colaboradores = []

    colaboradores.append(colaborador)

    with open("colaboradores.json","w") as arquivo:
        json.dump(colaboradores, arquivo, indent=4)

    print("\nColaborador salvo com sucesso!")

def listar_colaboradores(): #Listar Colaboradores
    with open("colaboradores.json", "r") as arquivo:
        colaboradores = json.load(arquivo)

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

while True:

    print("=== Sistema de RH ===")
    print("1 - Cadastrar Funcionário")
    print("2 - Listar Funcionários")
    print( "3 - Sair")
        
    opcao = input("Escolha uma opção.")
    if opcao == "1":
            print("Você escolheu cadastrar")
            cadastrar_colaborador()
        
    elif opcao == "2":
            print("Listando Funcionários")
            listar_colaboradores()

    elif opcao == "3":
            print("Sistema fechado")
            break