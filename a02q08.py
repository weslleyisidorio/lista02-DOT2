from random import choice
from string import ascii_uppercase


def preencherLista(qtdElementos):
    lista = []
    for i in range(qtdElementos):
        lista.append(choice(ascii_uppercase))

    return lista


def naLista(letra, lista):
    quantidade = 0
    for i in range(len(lista)):
        if lista[i] == letra:
            quantidade += 1

    return quantidade


def main():
    qtdElementos = 10
    listaLetras = preencherLista(qtdElementos)

    while True:
        try:
            letra = input("Digite uma letra: ").upper()
            if letra in ascii_uppercase:
                break
            else:
                print("Entrada inválida. Digite uma letra do alfabeto.")
        except ValueError:
            print("Entrada inválida. Digite uma letra maiúscula.")

    print(f"A letra {letra} aparece {listaLetras.count(letra)} "
          "vezes na lista.")
    print(f"A letra {letra} aparece {naLista(letra, listaLetras)} "
          "vezes na lista.")


if __name__ == "__main__":
    main()
