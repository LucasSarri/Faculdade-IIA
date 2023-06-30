import requests, json
#https://pixabay.com/api/docs/
url = "https://pixabay.com/api/?key=15467292-39beb0fec4e6919d4068c478e&q=happy&image_type=photo"

#na url acima, são enviados parâmetros como a chave de acesso e a busca (q)
resposta = requests.get(url).text

#print(resposta)
js = json.loads(resposta)

print(js['total'])

for h in js['hits']:
    print(h['pageURL'])
    print(h['tags'])
    print('-----------')