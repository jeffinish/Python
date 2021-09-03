## Arquivo Feito para fazer o levantamento dos ultimos concursos que ocorreram para professor de matemática em universidades federais, estaduais e municipais que possuem curso de Matemática (Seja licenciatura ou bacharelado)

### ---  Importando as bibliotecas necessárias --- ###
import pandas as pd

### --- Importando os arquivos necessários --- #

# Base de dados do Enade 2017 #
data = pd.read_csv("/home/jefferson/OneDrive/Pessoal/Python/Levantamento Matematica/enade_matematica_2017.csv")

data.columns

### --- Organização dos dados necessários --- ###
data["Categoria Administrativa"].drop_duplicates()
data["Categoria Administrativa"].value_counts()

### --- Avaliação das Universidades Públicas Municiapais --- ###
data.loc[data["Categoria Administrativa"] == "Pública Municipal"]
concursos = data.loc[data["Nome da IES"] == "UNIVERSIDADE REGIONAL DE BLUMENAU"].reset_index() #Aqui, defimos nosso novo dateset como sendo a linha que contém a primeira universidade publica municipal
colsdrop = [0,1,8,9,10,11]  #Lista de indices das colunas que a gente não precisa nesse caso
concursos = concursos.drop(concursos.columns[colsdrop],axis=1) #Dropamos as colunas baseadas no índice delas
concursos
for i in range(2020,2013,-1):  #Um loop muito maneiro (Que orgulho de mim) que inclui as colunas Ano_Vagas e Ano_Inscritos de 2020 até 2014 com o valor 0
    concursos.insert(len(concursos.columns),str(i)+"_Vagas",0)
    concursos.insert(len(concursos.columns),str(i)+"_Inscritos",0)
concursos.info()
concursos.head()

# - UNIVERSIDADE REGIONAL DE BLUMENAU - #
concursos.loc[0,"2016_Vagas"] = 1
concursos.loc[0,"2016_Inscritos"] = 13
concursos.loc[0,"2014_Vagas"] = 2+2
concursos.loc[0,"2014_Inscritos"] = 8+8
concursos
