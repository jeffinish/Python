### --- Importanto bibliotecas --- ###
import pandas as pd

### --- Importando bases de dados --- ###
veiculos = pd.read_csv(r"C:\Users\Jefferson Silva\OneDrive - ufmg.br\Pessoal\Python\Alura\Desafio_BI_Semana_1\Dados\Dados Brutos\Tabela-Veiculos.csv")

## -- Informações preliminares -- ##
veiculos.head()
veiculos.info()

### --- Tratamento dos dados --- ###
## -- Coloca o tipo de veiculo com a primeira letra maiúscula -- ##
veiculos.Tipo = veiculos.Tipo.str.capitalize()
veiculos.head()

## -- Ajusta o nome da coluna ID Veiculo -- ##
veiculos = veiculos.rename(columns={"ID veículos":"ID Veiculo"})
veiculos.head()

## -- Exporta o arquivo em CSV -- ##
veiculos.to_csv(r"C:\Users\Jefferson Silva\OneDrive - ufmg.br\Pessoal\Python\Alura\Desafio_BI_Semana_1\Dados\Dados Tratados\Tabela-Veiculos-Tratado.csv",index=False)
