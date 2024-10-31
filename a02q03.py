def preencher_Lista(quantidade):
    lista = []
    for i in range(quantidade):
        numero = int(input(f"Digite o {i + 1}º número: "))
        lista.insert(0, numero)

    return lista


def main():
    try:
        quantidade = int(input("Digite a quantidade de elementos da lista: "))
        if quantidade <= 0:
            raise ValueError("A quantidade de elementos da lista não pode "
                             "ser nula nem negativa.")
    except ValueError:
        print("A quantidade de elementos da lista deve ser um número "
              "inteiro positivo.")

    lista_Numeros = preencher_Lista(quantidade)
    print(lista_Numeros)


if __name__ == "__main__":
    main()
