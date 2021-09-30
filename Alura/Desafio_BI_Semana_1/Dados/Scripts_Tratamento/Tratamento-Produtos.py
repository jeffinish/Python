### --- Importanto bibliotecas --- ###
import pandas as pd

### --- Importando bases de dados --- ###
produtos = pd.read_csv(r"C:\Users\Jefferson Silva\OneDrive - ufmg.br\Pessoal\Python\Alura\Desafio_BI_Semana_1\Dados\Dados Brutos\Tabela-Produtos.csv")

## -- Informações preliminares -- ##
produtos.head()
produtos.info()

### --- Tratamento dos dados --- ###
## -- Separação do código do produto da descrição do produto utilizando split -- ##
produtos[["Código_Produto","Nome Produto"]] = produtos["categoria_produto"].str.split("-",expand=True)
produtos.head()

## -- Drop a coluna original categoria_produto -- ##
produtos = produtos.drop(["categoria_produto"],axis=1)
produtos.head()

## -- Coloca o nome do produto com a primeira letra maiúscula e troca os underlines por espaços
produtos["Nome Produto"] = produtos["Nome Produto"].str.capitalize()
produtos["Nome Produto"] = produtos["Nome Produto"].str.replace("_"," ")
produtos.head()

## -- Ajusta o nome das colunas -- ##
produtos = produtos.rename(columns={"preço":"Preço","Código_Produto":"Código do produto","Nome Produto":"Nome do produto"})
produtos = produtos.reindex(["Código do produto","Nome do produto","Preço"],axis=1)
produtos.head()

## -- Exporta o arquivo em CSV -- ##
produtos.to_csv(r"C:\Users\Jefferson Silva\OneDrive - ufmg.br\Pessoal\Python\Alura\Desafio_BI_Semana_1\Dados\Dados Tratados\Tabela-Produtos-Tratado.csv",index=False)
