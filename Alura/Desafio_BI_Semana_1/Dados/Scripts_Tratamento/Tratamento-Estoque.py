### --- Importanto bibliotecas --- ###
import pandas as pd

### --- Importando bases de dados --- ###
estoque = pd.read_csv(r"C:\Users\Jefferson Silva\OneDrive - ufmg.br\Pessoal\Python\Alura\Desafio_BI_Semana_1\Dados\Dados Brutos\Tabela-Estoque.csv")

## -- Informações preliminares -- ##
estoque.head()
estoque.info()

### --- Tratamento de dados --- ###
## -- Ajuste das informações da coluna Data atualização -- ##
estoque["Data atualização"] = estoque["Data atualização"].str.upper() #Mês maiúsculo
estoque["Data atualização"] = estoque["Data atualização"].str.replace("-","/") #Troca - por /
estoque["Data atualização"] = estoque["Data atualização"].str.replace(".","") #Remove o .
estoque.head()

## -- Exporta o arquivo em CSV -- ##
estoque.to_csv(r"C:\Users\Jefferson Silva\OneDrive - ufmg.br\Pessoal\Python\Alura\Desafio_BI_Semana_1\Dados\Dados Tratados\Tabela-Estoque-Tratado.csv",index=False)
