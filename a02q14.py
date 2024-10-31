from random import randint


def preencherLista(qntElementos):
    lista = []
    for i in range(qntElementos):
        lista.append(randint(-100, 100))

    return lista


def anulaNegativo(lista):
    listaMod = []
    for i in range(len(lista)):
        if lista[i] < 0:
            listaMod.append(0)
        else:
            listaMod.append(lista[i])

    return listaMod


def main():
    qtdElementos = 10
    listaC = preencherLista(qtdElementos)
    listaCMod = anulaNegativo(listaC)

    print(f"Lista original: {listaC}")
    print(f"Lista modificada: {listaCMod}")


if __name__ == '__main__':
    main()
