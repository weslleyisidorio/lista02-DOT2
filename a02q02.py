from random import randint


def gerar_Lista(quantidade):
    lista_Numeros = [randint(-100, 100) for i in range(quantidade)]

    return lista_Numeros


def contar_Negativos(lista):
    quantidade_Negativos = 0
    for elemento in lista:
        if elemento < 0:
            quantidade_Negativos += 1

    return quantidade_Negativos


def listar_Positivos(lista):
    lista_Positivos = []
    for elemento in lista:
        if elemento > 0:
            lista_Positivos.append(elemento)

    return lista_Positivos


def somatorio(lista):
    somatorio = 0
    for elemento in lista:
        somatorio += elemento

    return somatorio


def main():
    lista = gerar_Lista(10)

    qtd_Negativos = contar_Negativos(lista)
    print(qtd_Negativos)

    lista_Positivos = listar_Positivos(lista)
    soma_Positivos = somatorio(lista_Positivos)
    print(f"A soma dos elementos positivos é: {soma_Positivos}")


if __name__ == "__main__":
    main()
