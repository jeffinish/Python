### - Importanto bibliotecas - ###
import pandas as pd

### - Importando bases de dados - ###

produtos = pd.read_csv("/home/jefferson/OneDrive/Pessoal/Python/Alura/Desafio BI/Semana 1/Dados/Tabela - Produtos.csv")
produtos.head()
produtos.info()
produtos[["Código_Produto","Nome Produto"]] = produtos["categoria_produto"].str.split("-",expand=True,)
produtos.info()
produtos.head()
produtos = produtos.drop(["categoria_produto"],axis=1)
produtos.head()
produtos.to_csv("produtos-tratados.csv")
