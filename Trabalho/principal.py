import pandas as pd

alunos = []

def calculaMedia (notas):
    soma = 0
    for nota in notas:
        soma = soma + nota
    return soma/4


def processar_arquivo_xlsx(nome_arquivo):
    try:
        # Lê o arquivo XLSX em um DataFrame
        dados = pd.read_excel(nome_arquivo)

        # Verifica se as colunas necessárias estão presentes
        colunas_necessarias = ["Código do Aluno", "Nome", "Bimestre 1", "Bimestre 2", "Bimestre 3", "Bimestre 4"]
        if not all(coluna in dados.columns for coluna in colunas_necessarias):
            raise ValueError("O arquivo não possui todas as colunas necessárias")

        # Percorre as linhas e imprime as informações
        for indice, linha in dados.iterrows():
            bimestres = [linha[f"Bimestre {i}"] for i in range(1, 5)]
            media = calculaMedia(bimestres)
            aluno = {'codigo_aluno': linha["Código do Aluno"], 'nome': linha["Nome"], 'notas': bimestres, 'media': media}
            alunos.append(aluno)


    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except pd.errors.EmptyDataError:
        print(f"O arquivo '{nome_arquivo}' está vazio.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def verificaAprovacao (listaAlunos):
    for aluno in listaAlunos:
        if aluno['media'] < 6:
            print('O aluno {0} que possui a media {1} esta de exame'.format(aluno['nome'], aluno['media']))

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo XLSX
nome_arquivo_xlsx = 'Dados.xlsx'

# Chama a função com o nome do arquivo XLSX
processar_arquivo_xlsx(nome_arquivo_xlsx)
verificaAprovacao (alunos)
