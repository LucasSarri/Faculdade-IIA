import pandas as pd

tempo = pd.read_csv('weather_2012.csv',encoding = "ISO-8859-1")

print('Temperatura Maxima: ', max(tempo['Temp (C)']))
print('Temperatura Minima: ', min(tempo['Temp (C)']))
print('Condicoes Climaticas: ')
print(tempo['Weather'].unique)
