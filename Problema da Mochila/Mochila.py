import random
import time

start_time = time.time()

def geraListaItens():
    itens = []
    qtdItens = random.randint(2,20)
    for i in range(0, qtdItens):
        peso = random.randint(2,10)
        preco = random.randint(2,10)
        itens.append({'peso': peso, 'preco':preco})
    return itens

itens = geraListaItens()

PESO_MOCHILA = random.randint(8,20)
print('Peso Mochila: ', PESO_MOCHILA)

def geraPrimeirosIndividuos(n, tamanho):
    populacao = []
    for i in range(0, n):
        individuo = []
        pesoAtual = 0
        for j in range(0, tamanho):
            if pesoAtual <= PESO_MOCHILA:    
                individuo.append(1)
                pesoAtual = pesoAtual + itens[j]['peso']
            else:
                individuo.append(0)
        populacao.append({"individuo":individuo, "avaliacao":avalia(individuo)})
    return populacao
    
def avalia(individuo):
    aval = {'peso':0, 'preco':0}
    for i in range(0,len(individuo)):
        if(individuo[i] == 1):
            aval['peso']  += itens[i]['peso']
            aval['preco'] += itens[i]['preco']
    return aval['preco']

def pesoPreco(individuo):
    aval = {'peso':0, 'preco':0}
    for i in range(0,len(individuo)):
        if(individuo[i] == 1):
            aval['peso']  += itens[i]['peso']
            aval['preco'] += itens[i]['preco']
    return aval
            

def reproduz(pai, mae):
    posCorte = random.randint(0, len(pai['individuo']))
    filho = []
    for i in range(0, posCorte):
        filho.append(pai['individuo'][i])
    for i in range(posCorte, len(pai['individuo'])):
        filho.append(mae['individuo'][i])     
    mutacao = random.randint(0,1)
    posMutacao = random.randint(0, len(filho)-1)
    if mutacao == 1:
        filho[posMutacao] = 1
    return {'individuo':filho, 'avaliacao': avalia(filho)}

def run(populacao, max):
    satisfeito = False
    populacao.sort(key=lambda x:x['avaliacao'], reverse=True) 
    geracao = 0
    while not satisfeito:
        novaPopulacao = []
        for i in populacao:
            maxPos = random.randint(0, len(populacao)/2)
            x = populacao[random.randint(0,maxPos)]
            y = populacao[random.randint(0,maxPos)]
            filho = reproduz(x, y)
            novaPopulacao.append(filho)
        populacao = novaPopulacao
        populacao.sort(key=lambda x:x['avaliacao'], reverse=True)
        geracao += 1
        if(geracao >= max):
            satisfeito = True
    print(populacao)
    return populacao[0]

qtdIndividuos = random.randint(4,12)
print('Quantidade de Individuos: ', qtdIndividuos, 'Tamanho Individuos: ', len(itens))
populacao = geraPrimeirosIndividuos(qtdIndividuos, len(itens))
melhor = run(populacao, 7000)
print("Melhor configuração: ")
print(melhor)
print("Peso e preço: ")
print(pesoPreco(melhor['individuo']))
end_time = time.time()
execution_time = end_time - start_time
print(f"O programa demorou {execution_time:.2f} segundos para ser executado.")
