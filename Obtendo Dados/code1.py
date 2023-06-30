#https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
import pandas as pd
#import matplotlib.pyplot as plt
#https://www.kaggle.com/adityapatil673/classification-traits-of-a-poisonous-mushroom/notebook
#First column is a classifier
#Class : edible e, poisonous p
#Rest of the columns are
#cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s
#cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s
#cap-color: brown=n,buff=b,cinnamon=c,gray=g,green=r, pink=p,purple=u,red=e,white=w,yellow=y
#bruises?: bruises=t,no=f
#odor: almond=a,anise=l,creosote=c,fishy=y,foul=f, musty=m,none=n,pungent=p,spicy=s ....

cogumelos = pd.read_csv('mushrooms.csv',encoding = "ISO-8859-1")#lê o arquivo

#print(cogumelos.head())#imprime o cabeçalho




#print(cogumelos['cap-shape'])#imprime a coluna class


#print("unique: " + str(cogumelos['cap-shape'].unique()))#valores únicos na coluna


#substitui 'p' por 1 e 'e' por 0
cogumelos['class'] = cogumelos['class'].map({'p':1, 'e':0})


#imprime novamente
#print(cogumelos['class'])


#mostra os valores únicos existentes..
#print("unique: " + str(cogumelos['class'].unique()))

#plota
#cogumelos['class'].plot()

print(cogumelos['class'].count())#conta quantidade total

#pandas usa o matplotlib, tem que chamar o show
#plt.show()

#print(cogumelos.sum())
