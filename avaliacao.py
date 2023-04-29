#Façam para uma lista de N elementos;
def avalia(itens, mochila):
    peso = 0
    preco = 0

    if (len(mochila) != len(itens)):
        print('Erro: o tamanho da mochila deve ser igual ao tamanho da lista de itens')
        return [-1, -1]

    for i in range(0, len(mochila)):
        if mochila[i] == 1:
            peso = peso + itens[i]['peso']
            preco = preco + itens[i]['preco']

    return [peso, preco]