# from random import randint


def preencherLista(quantidade):
    lista = []
    for i in range(quantidade):
        try:
            lista.append(int(input(f"Digite o {i+1}º elemento: ")))
            # lista.append(randint(0, 100))
        except ValueError:
            print("Entrada inválida. Digite um númerointeiro.")
            i -= 1

    return lista


def unir(lista1, lista2):
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])

    return lista3


def unir2(lista1, lista2):
    lista3 = [0] * (len(lista1) + len(lista2))
    for i in range(len(lista1)):
        lista3[2*i] = lista1[i]
        lista3[2*i+1] = lista2[i]

    return lista3


def main():
    qtdEmentos = 10
    lista1 = preencherLista(qtdEmentos)
    lista2 = preencherLista(qtdEmentos)
    lista3 = unir(lista1, lista2)
    print(f"lista 3: {lista3}")
    lista4 = unir2(lista1, lista2)
    print(f"lista 4: {lista4}")


if __name__ == "__main__":
    main()
