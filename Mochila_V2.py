import random
import time

start_time = time.time()

def gerarListaItens():
    quantidadeItens = random.randint(2, 10)
    listaItens = []
    for i in range(0, quantidadeItens):
        peso = random.randint(1, 10)
        preco = random.randint(1, 10)
        listaItens.append({'peso': peso, 'preco':preco})
    return listaItens

itens = gerarListaItens()
print('Lista de Itens: ',itens)

def avaliaListaItens(itens):
    avaliacaoItens = []
    for i in itens:
        avaliacaoItens.append(i['preco']/i['peso'])
    return avaliacaoItens

def avaliaIndividuo(individuo, pesoMaximo):
    aval = {'peso':0, 'preco':0}
    for i in range(0, len(individuo)):
        if(individuo[i] == 1):
            aval['peso']  += itens[i]['peso']
            aval['preco'] += itens[i]['preco']
    if(aval['peso'] > pesoMaximo):
        return -1
    else:
        return aval['preco']

def geraIndividuos(n, tamanho, pesoMaximo, itens,avaliacaoItens):
    populacao = []
    avaliacao = 0
    posAvaliacao = 0
    for i in range(0, n):
        individuo = []
        for j in range(0, tamanho):
            for k in range(0, len(avaliacaoItens)):
                if avaliacaoItens[k] >= avaliacao:
                    avaliacao = avaliacaoItens[k]
                    posAvaliacao = k
            if itens[posAvaliacao]['peso'] <= pesoMaximo:
                individuo.append(1)
            else:
                individuo.append(0)
        populacao.append({"individuo":individuo, "avaliacao":avaliaIndividuo(individuo)})

avaliacaoItens = avaliaListaItens(itens)
primeirosIndividuos = geraIndividuos(8, 7, 13, itens,avaliacaoItens)

def reproduz(pai, mae):