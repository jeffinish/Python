# Arquivo para analisar arquivos do enade pra Matemática
import pandas as pd #Importa o Panda para trabalhar com o arquivo Excel
import plotly.express as px #Importa o Plotly para fazer gráficos e histogramas
from googlesearch import search #Importa a API do google pra procurar

pd.set_option("display.max_rows",10) #Seta o máximo de linhas para ser exibida
pd.set_option("display.max_columns",5) #Seta o máximmo de colunas para ser exibida

df2014 = pd.read_csv("enade_matematica_2014.csv") #Abre o arquivo csv
df2017 = pd.read_csv("enade_matematica_2017.csv") #Abre o arquivo csv
#print(df2014.info())
#print(df2017.info())
print(df2014.columns)
print(df2017.columns)

cols = df2017.columns
#print(cols)
df2014 = df2014[cols]

MAT = pd.concat([df2014,df2017],axis=0).reset_index(drop=True)
print(MAT.info())

MAT.to_csv("enade_matematica_1417.csv",index=False)
