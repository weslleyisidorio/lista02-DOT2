def preencherLista(qtdElementos):
    lista = []
    for i in range(qtdElementos):
        while True:
            try:
                entrada = int(input(f"Digite o {i + 1}º número: "))
                lista.append(entrada)
                break
            except ValueError:
                print("Digite um número inteiro válido.")

    return lista


def valoresNegativos(lista):
    listaMod = []
    for i in range(len(lista)):
        if lista[i] < 0:
            listaMod.append(lista[i])

    return listaMod


def main():
    qtdeElementos = 10
    listaX = preencherLista(qtdeElementos)
    listaR = valoresNegativos(listaX)

    print("----------------------------------")
    print(f"Lista original: {listaX}")
    print(f"Valores negativos: {listaR}")


if __name__ == "__main__":
    main()
