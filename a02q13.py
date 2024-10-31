from random import randint


def lancarDado(qntLancamentos):
    lancamentos = []
    for i in range(qntLancamentos):
        lancamentos.append(randint(1, 6))

    return lancamentos


def calcOcorrencias(lancamentos):
    ocorrencias = [0, 0, 0, 0, 0, 0]
    for i in range(len(lancamentos)):
        ocorrencias[lancamentos[i] - 1] += 1

    return ocorrencias


def main():
    qntLancamentos = 10
    lancamentos = lancarDado(qntLancamentos)
    ocorrencias = calcOcorrencias(lancamentos)
    print(f"Lançamentos: {lancamentos}")
    print(f"Ocorrências: \n"
          f"1: {ocorrencias[0]}\n"
          f"2: {ocorrencias[1]}\n"
          f"3: {ocorrencias[2]}\n"
          f"4: {ocorrencias[3]}\n"
          f"5: {ocorrencias[4]}\n"
          f"6: {ocorrencias[5]}")


if __name__ == '__main__':
    main()
