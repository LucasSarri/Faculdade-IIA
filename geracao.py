import random

def geraMochila(itens):
    mochila = []

    for i in range(0, len(itens)):
        valor = random.randint(0,1)
        mochila.append(valor)

    return mochila

def geraItens ():
    itens = []

    tamanhoListaItens = random.randint(2,10)

    for i in range(0, tamanhoListaItens):
        peso = random.randint(1,8)
        preco = random.randint(1,8)

        itens.append({'peso': peso, 'preco': preco})

    return itens