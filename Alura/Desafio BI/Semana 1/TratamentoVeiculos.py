### - Importanto bibliotecas - ###
import pandas as pd

### - Importando bases de dados - ###

veiculos = pd.read_csv("/home/jefferson/OneDrive/Pessoal/Python/Alura/Desafio BI/Semana 1/Dados/Tabela - Veículos.csv")
veiculos.head()
veiculos.Tipo = veiculos.Tipo.str.upper()
veiculos.head()
veiculos.to_csv("veiculos-tratado.csv")
