def preencherLista(qtdElemtos):
    lista = []
    for i in range(qtdElemtos):
        while True:
            try:
                lista.append(int(input(f"Digite o {i+1}º elemento: ")))
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    return lista


def inverterLista(lista):
    listaInvertida = []
    for i in range(len(lista) - 1, -1, -1):
        listaInvertida.append(lista[i])

    return listaInvertida


def main():
    qtdElemtos = 5
    listaX = preencherLista(qtdElemtos)
    listaY = inverterLista(listaX)
    print(f"Lista X: {listaX}")
    print(f"Lista Y: {listaY}")


if __name__ == "__main__":
    main()
