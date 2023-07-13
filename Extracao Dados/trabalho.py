#Alunos: Lucas Sarri e Lucas Lopes
import funcoesGerais

dados = funcoesGerais.extraiDados()
contador = funcoesGerais.criaCont()
contador = funcoesGerais.contagem(dados, contador)
numerosSorteados = funcoesGerais.maisSorteados(contador)
print(numerosSorteados)
