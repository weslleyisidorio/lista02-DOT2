from random import randint


def preencherLista(qntElementos):

    """
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
    """

    lista = []
    for i in range(qntElementos):
        lista.append(randint(-100, 100))

    return lista


def copiarListas(lista1, lista2):
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i])
    for j in range(len(lista2)):
        lista3.append(lista2[j])

    return lista3


def main():
    listaR = preencherLista(5)
    listaS = preencherLista(10)
    listaX = copiarListas(listaR, listaS)

    print("----------------------------------")
    print(f"Lista R: {listaR}")
    print(f"Lista S: {listaS}")
    print(f"Lista X: {listaX}")


if __name__ == "__main__":
    main()
