def preencher_Lista():
    lista = []

    for i in range(15):
        try:
            numero = int(input(f"Digite o {i+1}º número: "))
            lista.append(numero)

        except ValueError:
            print("Digite um número inteiro!")
            continue

    return lista


def maior(lista):
    maior = 0
    for indice, elemento in enumerate(lista):
        if lista[maior] < elemento:
            maior = indice

    return maior


def menor(lista):
    menor = 0
    for indice, elemento in enumerate(lista):
        if lista[menor] > elemento:
            menor = indice

    return menor


def main():
    lista = preencher_Lista()
    idMaior = maior(lista)
    idMenor = menor(lista)
    print(f"O maior número é {lista[idMaior]}, que é o {idMaior+1} "
          "elemento da lista.")
    print(f"O menor número é {lista[idMenor]}, que é o {idMenor+1} "
          "elemento da lista.")


if __name__ == "__main__":
    main()
