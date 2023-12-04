import numpy as np
import matplotlib.pyplot as mp

# Nota do aluno - linhas
def graphAlunoScatter(nota,nome):
  y = [nota[0],nota[1],nota[2],nota[3]]
  x = ['P1','P2','P3','P4']
  mp.title("Notas - "+nome)
  mp.ylabel('Notas')
  mp.xlabel('Provas')
  mp.scatter(x,y)
  mp.plot(x,y, linestyle = '-')
  print('')
  mp.show()

def graphMediaAluno(alunoAna,alunoBea,alunoCaio,alunoDanilo):
  mediaAna = np.mean(alunoAna)
  mediaBeatriz = np.mean(alunoBea)
  mediaCaio = np.mean(alunoCaio)
  mediaDanilo = np.mean(alunoDanilo)

  y = [mediaAna,mediaBeatriz,mediaCaio,mediaDanilo]
  x = ['Ana da Silva','Beatriz da Silva','Caio da Silva','Danilo da Silva']

  mp.title('Média dos Alunos')
  mp.ylabel('Média')
  mp.xlabel('Alunos')
  mp.bar(x,y)
  print('')
  mp.show()




listaAna = [7.7,5.1,8.5,9.0]
listaBeatriz = [7.3,5.3,6.0,9.0]
listaCaio = [4.2,5.6,3.0,5.0]
listaDanilo = [9.1,7.9,8.0,7.5]

aluno1 = 'Ana da Silva'
aluno2 = 'Beatriz da Silva'
aluno3 = 'Caio da Silva'
aluno4 = 'Danilo da Silva'

# Gráfico em linha das notas dos alunos 
graphAlunoScatter(listaAna,aluno1)
graphAlunoScatter(listaBeatriz,aluno2)
graphAlunoScatter(listaCaio,aluno3)
graphAlunoScatter(listaDanilo,aluno4)

print('')
print('')
print('')

graphMediaAluno(listaAna,listaBeatriz,listaCaio,listaDanilo)