def preencherLista(qntElementos):
    lista = []

    for i in range(qntElementos):
        while True:
            try:
                entrada = int(input(f"Digite o {i + 1}º número: "))
                if entrada > 0:
                    lista.append(entrada)
                    break
                else:
                    raise ValueError

            except ValueError:
                print("Digite um número inteiro maior que 0.")

    return lista


def revisaLista(lista):
    listaMod = []
    for i in range(len(lista)):
        if i % 2 == 0:
            listaMod.append(round(lista[i] / 2, 1))
        else:
            listaMod.append(lista[i] * 3)

    return listaMod


def main():
    qntElementos = 10

    print("----------------------------------")

    listaX = preencherLista(qntElementos)
    print(f"Lista original: {listaX}")

    listaY = revisaLista(listaX)
    print(f"Lista modificada: {listaY}")


if __name__ == '__main__':
    main()
