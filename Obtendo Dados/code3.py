from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.example.com").text
soup = BeautifulSoup(html, 'html5lib')



#retorna o primeiro parágrafo
paragrafo = soup.find('p')

print(paragrafo)

#retorna todos parágrafos:
paragrafos = soup.find_all('p')
print(paragrafos)

#acessar propriedades
#print(paragrafo['id'])

#for p in soup('p'):
#    print("paragrafo: " + str(p.text))


print(soup('a'))
print(soup.find('a')['href'])