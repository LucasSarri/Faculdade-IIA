from bs4 import BeautifulSoup

with open('mega.mhtml', 'r') as file:
    html =  file.read()

soup = BeautifulSoup(html, 'html5lib')

resultados = soup.find_all('tr')

indiceLinha = 1
vetorLinhas = []

while indiceLinha < len(resultados):
    indiceColuna = 1
    vetorColunas = []

    colunas = resultados[indiceLinha].find_all('td')
   
    if (len(colunas) >= 7):
        while indiceColuna <= 7:
            vetorColunas.append(colunas[indiceColuna].get_text())
            indiceColuna = indiceColuna + 1
            
    if (vetorColunas != []):
        vetorLinhas.append(vetorColunas)

    indiceLinha = indiceLinha + 1

print(vetorLinhas)
