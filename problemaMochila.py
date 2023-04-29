import geracao
import avaliacao

itens = geracao.geraItens ()
mochila = geracao.geraMochila(itens)

av = avaliacao.avalia(itens, mochila)

print('Peso: '+str(av[0])+' Preco: '+str(av[1]))