import heapq
from bs4 import BeautifulSoup

def extraiDados():
    # Abre o arquivo
    with open('mega.mhtml', 'r') as file:
        html =  file.read()
    # Aplicando o conversor para entender o html
    soup = BeautifulSoup(html, 'html5lib')
    # Buscando todas as linhas da tabela
    resultados = soup.find_all('tr')
    # Criando variáveis do vetor de linhas e do indice da linha
    indiceLinha = 1
    vetorLinhas = []
    # Laço para percorrer todas as linhas
    while indiceLinha < len(resultados):
        # Criando variáveis do indice de colunas e vetor de colunas
        indiceColuna = 2
        vetorColunas = []
        # Buscando todas as colunas
        colunas = resultados[indiceLinha].find_all('td')
        # Conferindo se a linha tem mais de 7 colunas
        if (len(colunas) >= 7):
            # Retornando os dados das colunas 1 ao 7
            while indiceColuna <= 7:
                # Pegando o texto dentro das colunas e removendo lixo
                elemento = colunas[indiceColuna].get_text().strip('=\n')
                elemento = elemento.strip('<=\n/td>')
                if(indiceColuna >= 2):
                    # Adicionando o elemento na lista de colunas
                    vetorColunas.append(int(elemento))
                else:
                    vetorColunas.append(elemento)
                indiceColuna = indiceColuna + 1
        # Verificando se o vetor de colunas não esta vazio          
        if (vetorColunas != []):
            # Inserindo o vetor de colunas no vetor de linhas
            vetorLinhas.append(vetorColunas)
        indiceLinha = indiceLinha + 1
    return vetorLinhas

def criaCont():
    cont = []
    i = 0

    while i < 60:
        cont.append(0)
        i = i + 1

    return cont

def contagem(lista, cont):
    for i in lista:
        for j in i:
            cont[j-1] = cont[j-1] + 1
    return cont

def maisSorteados(cont):
    indices_maiores = heapq.nlargest(6, range(len(cont)), key=cont.__getitem__)
    j = 0
    for i in indices_maiores:
        indices_maiores[j] = i+1
        j = j+1
    return indices_maiores
