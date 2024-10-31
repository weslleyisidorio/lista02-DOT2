# from random import randint


def preencherLista(qntElementos):
    lista = []

    for i in range(qntElementos):
        while True:
            try:
                entrada = int(input(f"Digite o {i + 1}º número: "))
                lista.append(entrada)
                break
            except ValueError:
                print("Digite um número inteiro válido.")

    return lista


''' for i in range(qntElementos):
        lista.append(randint(-100, 100))

    return lista
'''


def invertList(lista):
    listaInvert = []
    for i in range(len(lista) - 1, -1, -1):
        listaInvert.append(lista[i])

    return listaInvert


def main():
    qntElementos = 10
    listaD = preencherLista(qntElementos)
    listaE = invertList(listaD)
    print(f"Lista original: {listaD}")
    print(f"Lista invertida: {listaE}")


if __name__ == '__main__':
    main()
