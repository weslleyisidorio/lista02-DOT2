from random import choice

alternativas = ['a', 'b', 'c', 'd', 'e']


def gerarGabarito(quantQuestoes):
    gerarGabarito = []
    for i in range(quantQuestoes):
        gerarGabarito.append(choice(alternativas).upper())

    return gerarGabarito


def gerarRespostas(quantidadeAlunos):
    respostas = []
    for i in range(quantidadeAlunos):
        respostas.append(gerarGabarito(30))

    return respostas


def compararGabarito(gabarito, respostas):
    quantidadeAcertos = []
    for i in range(len(respostas)):
        acertos = 0
        for j in range(len(respostas[i])):
            if respostas[i][j] == gabarito[j]:
                acertos += 1
        quantidadeAcertos.append(acertos)

    return quantidadeAcertos


def main():
    quantQuestoes = 30
    gabarito = gerarGabarito(quantQuestoes)

    quantidadeAlunos = 10
    respostas = gerarRespostas(quantidadeAlunos)

    quatidadeAcertos = compararGabarito(gabarito, respostas)
    print(f"Acertos por aluno: {quatidadeAcertos}")


if __name__ == '__main__':
    main()
