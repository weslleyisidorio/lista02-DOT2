from random import randint


def preencherLista(qtdElemtos):
    lista = []
    for i in range(qtdElemtos):
        while True:
            try:
                # lista.append(int(input(f"Digite o {i+1}º elemento: ")))
                lista.append(randint(0, 100))
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    return lista


def maior(lista):
    maiorElemtento = lista[0]
    posicaoMaior = 0
    for i in range(1, len(lista)):
        if lista[i] > maiorElemtento:
            maiorElemtento = lista[i]
            posicaoMaior = i

    return maiorElemtento, posicaoMaior


def menor(lista):
    menorElemtento = lista[0]
    posicaoMenor = 0
    for i in range(1, len(lista)):
        if lista[i] < menorElemtento:
            menorElemtento = lista[i]
            posicaoMenor = i

    return menorElemtento, posicaoMenor


def main():
    qtdElemtos = 15
    lista1 = preencherLista(qtdElemtos)
    maiorElemtento, posicaoMaior = maior(lista1)
    menorElemtento, posicaoMenor = menor(lista1)
    print(f"Lista: {lista1}")
    print(f"O maior elemento é {maiorElemtento} e está na posição "
          f"{posicaoMaior}.")
    print(f"O menor elemento é {menorElemtento} e está na posição "
          f"{posicaoMenor}.")


if __name__ == "__main__":
    main()
