from random import randint


def preencherLista(qtdEmentos):
    lista = []
    for i in range(qtdEmentos):
        try:
            # lista.append(int(input(f"Digite o {i+1}º elemento: ")))
            lista.append(randint(0, 100))
        except ValueError:
            print("Entrada inválida. Digite um númerointeiro.")
            i -= 1

    return lista


def naLista(numero, lista):
    quantidade = 0
    for i in range(len(lista)):
        if lista[i] == numero:
            quantidade += 1

    return quantidade


def main():
    qtdEmentos = 10
    lista1 = preencherLista(qtdEmentos)
    while True:
        try:
            numero = int(input("Digite um número: "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    print(f"O número {numero} aparece {lista1.count(numero)} vezes na lista.")
    print(f"O número {numero} aparece {naLista(numero, lista1)} "
          "vezes na lista.")


if __name__ == "__main__":
    main()
