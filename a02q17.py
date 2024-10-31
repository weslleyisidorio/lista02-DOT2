def preencherLista(qntElementos):
    lista = []

    for i in range(qntElementos):
        while True:
            try:
                entrada = int(input(f"Digite o {i + 1}º número: "))
                lista.append(entrada)
                break

            except ValueError:
                print("Digite um número inteiro.")

    return lista


def validaEntrada():
    while True:
        try:
            valor = int(input("Digite um valor inteiro: "))
            return valor
        except ValueError:
            print("Digite um valor inteiro maior que 0.")


def repete(lista, valor):
    repeticoes = 0
    indices = []

    for i in range(len(lista)):
        if lista[i] == valor:
            repeticoes += 1
            indices.append(i)

    if repeticoes > 0:
        return f"Repeticoes: {repeticoes} nos indices {indices}"
    else:
        return "Valor não encontrado."


def main():
    qntElementos = 10
    listaW = preencherLista(qntElementos)
    valor = validaEntrada()
    repeticoes = repete(listaW, valor)

    print("----------------------------------")

    print(f"O valor {valor} aparece {repeticoes} vezes na lista.")
    print(repeticoes)


if __name__ == "__main__":
    main()
