from random import randint, random


def preencherQuantidade(n):
    quantidade = []
    for i in range(n):
        try:
            # quantidade.append(int(input(f"Digite a quantidade do "
            #                           "{i+1}º produto: ")))
            quantidade.append(randint(0, 20))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            i -= 1

    return quantidade


def preencherPrecos(n):
    preco = []
    for i in range(n):
        try:
            # preco.append(float(input(f"Digite o preço do {i+1}º produto: ")))
            preco.append(round(random() * 100, 2))
        except ValueError:
            print("Entrada inválida. Digite um número real.")
            i -= 1

    return preco


def faturar(quantidade, preco):
    faturamento = 0
    for i in range(len(quantidade)):
        faturamento += quantidade[i] * preco[i]

    return faturamento


def comparar(preco, faturamento):
    faturamentosAbaixo = []
    for i in range(len(preco)):
        if preco[i] < faturamento:
            faturamentosAbaixo.append(preco[i])

    return faturamentosAbaixo


def faturaMed(faturamento, quantidade):
    n = 0

    for i in range(len(quantidade)):
        n += quantidade[i]

    return faturamento / n


def main():
    elementos = 20
    quantidade = preencherQuantidade(elementos)
    preco = preencherPrecos(elementos)
    faturamentoTotal = faturar(quantidade, preco)
    faturamentoMedio = faturaMed(faturamentoTotal, quantidade)
    faturamentosAbaixo = comparar(preco, faturamentoMedio)

    print(f"Quantidade: {quantidade}")
    print(f"Preços: {preco}")
    print(f"Faturamento total: {faturamentoTotal:.2f}")
    print(f"Faturamento médio: {faturamentoMedio:.2f}")

    print(f"Faturamentos abaixo da média: {faturamentosAbaixo}")


if __name__ == "__main__":
    main()
