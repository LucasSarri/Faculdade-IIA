import random
import time

start_time = time.time()

itens = [
    {'peso': 6, 'preco':2},
    {'peso': 3, 'preco':7},
    {'peso': 1, 'preco':3},
    {'peso': 7, 'preco':4},
    {'peso': 4, 'preco':5},
    {'peso': 2, 'preco':2},
    {'peso': 5, 'preco':6},
]
print(itens)
PESO_MOCHILA = 13

def geraPrimeirosIndividuos(n, tamanho):
    populacao = []
    for i in range(0, n):
        individuo = []
        for j in range(0, tamanho):
            individuo.append(random.randint(0,1))
        populacao.append({"individuo":individuo, "avaliacao":avalia(individuo)})
    return populacao
    
def avalia(individuo):
    aval = {'peso':0, 'preco':0}
    for i in range(0,len(individuo)):
        if(individuo[i] == 1):
            aval['peso']  += itens[i]['peso']
            aval['preco'] += itens[i]['preco']
    if(aval['peso'] > PESO_MOCHILA):
        return 0
    else:
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
    return {'individuo':filho, 'avaliacao': avalia(filho)}

def run(populacao, max):
    satisfeito = False
    populacao.sort(key=lambda x:x['avaliacao'], reverse=True) #ordena por avaliacao
    geracao = 0
    while not satisfeito:
        novaPopulacao = []
        
        for i in populacao:#para cada individuo...
            maxPos = random.randint(0, len(populacao)/2) #até a metade... os melhores estão no começo.
            x = populacao[random.randint(0,maxPos)]
            y = populacao[random.randint(0,maxPos)]
            filho = reproduz(x, y)

            novaPopulacao.append(filho)
        populacao = novaPopulacao
        populacao.sort(key=lambda x:x['avaliacao'], reverse=True) #ordena por avaliacao
        geracao += 1
        if(geracao >= max):
            satisfeito = True
    print(populacao)
    return populacao[0]
            




populacao = geraPrimeirosIndividuos(8,7)

melhor = run(populacao, 1000)

print("Melhor configuração: ")

print(melhor)
print("Peso e preço: ")
print(pesoPreco(melhor['individuo']))

end_time = time.time()
execution_time = end_time - start_time

print(f"O programa demorou {execution_time:.2f} segundos para ser executado.")
