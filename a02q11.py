def menu():
    print("------------------------------------")
    print("1 - Inserir contato")
    print("2 - Buscar contato")
    print("3 - Listar contatos")
    print("0 - Sair")
    print("------------------------------------")

    while True:
        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao < 0 or opcao > 3:
                print("Opção inválida. Digite um número entre 0 e 3.")
                return menu()
            break

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            return menu()

    return opcao


def cadastrarNome(nomes):
    nome = input("Digite o nome: ")
    nomes.append(nome)
    print("Nome cadastrado com sucesso.")
    print("------------------------------------")


def buscarNome(nomes):
    nome = input("Digite o nome que deseja buscar: ")
    if nome in nomes:
        print(f"O nome {nome} foi encontrado.")
    else:
        print(f"O nome {nome} não foi encontrado.")
    print("------------------------------------")


def listarNomes(nomes):
    if len(nomes) == 0:
        print("Nenhum nome cadastrado.")
    else:
        print("Nomes cadastrados:")
        for nome in nomes:
            print(nome)
    print("------------------------------------")


def main():
    nomes = []

    while True:
        opcao = menu()

        if opcao == 1:
            cadastrarNome(nomes)
        elif opcao == 2:
            buscarNome(nomes)
        elif opcao == 3:
            listarNomes(nomes)
        else:
            print("Saindo do programa.")
            exit()


if __name__ == "__main__":
    main()
