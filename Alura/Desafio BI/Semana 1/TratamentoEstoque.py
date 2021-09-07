### - Importanto bibliotecas - ###
import pandas as pd

### - Importando bases de dados - ###

estoque = pd.read_csv("/home/jefferson/OneDrive/Pessoal/Python/Alura/Desafio BI/Semana 1/Dados/Tabela - Estoque.csv")
estoque.head()
estoque.info()
estoque["Data atualização"].drop_duplicates()
estoque["Data atualização"] = estoque["Data atualização"].str.upper()
estoque["Data atualização"] = estoque["Data atualização"].str.replace("-","/")
estoque["Data atualização"] = estoque["Data atualização"].str.replace(".","")
estoque.head()
estoque.to_csv("estoque-tratado.csv")
