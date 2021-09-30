### --- Importanto bibliotecas --- ###
import pandas as pd

### --- Importando bases de dados --- ###
pedidos = pd.read_csv(r"C:\Users\Jefferson Silva\OneDrive - ufmg.br\Pessoal\Python\Alura\Desafio_BI_Semana_1\Dados\Dados Brutos\Tabela-Pedidos.csv",sep=";",encoding='latin-1')

## -- Informações preliminares -- ##
pedidos.head()
pedidos.info()

## -- Ajusta o nome da coluna ID Veiculo -- ##
pedidos = pedidos.rename(columns={"ID Veículos":"ID Veiculo"})
pedidos.head()

## -- Exporta o arquivo em CSV -- ##
pedidos.to_csv(r"C:\Users\Jefferson Silva\OneDrive - ufmg.br\Pessoal\Python\Alura\Desafio_BI_Semana_1\Dados\Dados Tratados\Tabela-Pedidos-Tratado.csv",index=False)
