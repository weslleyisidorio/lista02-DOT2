from random import randint


def gerar_Lista(quantidade):
    elementos = []
    elementos = [randint(-100, 100) for i in range(quantidade)
                 if randint(-100, 100) not in elementos]

    return elementos


def contar_Pares(lista):
    pares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1

    return f"Quantidade de pares: {pares}"


def listar_NPares(lista):
    lista_Pares = []
    for elemento in lista:
        if elemento % 2 == 0:
            lista_Pares.append(elemento)

    return lista_Pares


def contar_Impares(lista):
    impares = 0
    for numero in lista:
        if numero % 2 != 0:
            impares += 1

    return f"Quantidade de ímpares: {impares}"


def listar_NImpares(lista):
    lista_Ipares = []
    for elemento in lista:
        if elemento % 2 != 0:
            lista_Ipares.append(elemento)

    return lista_Ipares


def main():
    lista = gerar_Lista(100)

    print(contar_Pares(lista))
    lista_Pares = listar_NPares(lista)
    print(lista_Pares)

    print("------------------------------------")

    print(contar_Impares(lista))
    lista_impares = listar_NImpares(lista)
    print(lista_impares)


if __name__ == "__main__":
    main()
