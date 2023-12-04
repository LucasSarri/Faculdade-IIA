import pandas as pd

alunos = []

def processar_arquivo_xlsx(nome_arquivo):
    dados = pd.read_excel(nome_arquivo)

    for indice, linha in dados.iterrows():
        bimestres = [linha[f"Bimestre {i}"] for i in range(1, 5)]
        media = calculaMedia(bimestres)
        aprovado = verificaAprovacao (media)
        aluno = {'codigo_aluno': linha["Codigo do Aluno"], 'nome': linha["Nome"], 'notas': bimestres, 'media': media, 'aprovacao': aprovado}
        alunos.append(aluno)


def calculaMedia (notas):
    soma = 0
    for nota in notas:
        soma = soma + nota
    return soma/4

def verificaAprovacao (media):
    if media >= 6:
        return "aprovado"
    elif (media < 6 and media >= 3):
        return "de exame"
    else:
        return "reprovado"
    

nome_arquivo_xlsx = 'Dados.xlsx'

processar_arquivo_xlsx(nome_arquivo_xlsx)

for aluno in alunos:
    print("O aluno {0} com o código {1}, possuí as notas: {2}, tendo como média {3}, estando {4}\n".format(aluno['codigo_aluno'],aluno['nome'],aluno['notas'],aluno['media'],aluno['aprovacao']))