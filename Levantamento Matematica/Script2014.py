# Arquivo para analisar arquivos do enade pra Matemática
import pandas as pd #Importa o Panda para trabalhar com o arquivo Excel
import plotly.express as px #Importa o Plotly para fazer gráficos e histogramas
from googlesearch import search #Importa a API do google pra procurar

pd.set_option("display.max_rows",10) #Seta o máximo de linhas para ser exibida
pd.set_option("display.max_columns",5) #Seta o máximmo de colunas para ser exibida

#Definir as colunas Relevantes:
# - Ano
# - Código da Área
# - Área de Avaliação
# - Código da IES
# - Sigla da IES
# - Organização Acadêmica
# - Categoria Administrativa
# - Modalidade de Ensino
# - Município do curso
# - Sigla da UF -> Estado
# - Numero de Concluintes Inscritos -> Concluintes Inscritos
# - Número de Concluintes Participantes -> Concluintes Participantes
# - Conceito Enade (Contínuo)
# - Conceito Enade (Faixa)

# Ano : 2014
df = pd.read_excel("resultados_conceito_enade_2014.xlsx") #Abre o arquivo xlxs
df = df.drop(["Nota Bruta - FG","Nota Padronizada - FG",
                "Nota Bruta - CE", "Nota Padronizada - CE",
                "Nota Bruta - Geral", "Nota Padronizada - Geral", "Cod. Município",
                "Observação"],axis=1) #Dropa algumas colunas
df = df.rename(columns={"Cód Area":"Código da Área","Área":"Área de Avaliação",
                        "Cód. IES":"Código da IES","Nº de Concluintes Inscritos":"Concluintes Inscritos",
                        "Nº  de Concluintes Participantes":"Concluintes Participantes",
                        "Nome do Município":"Município do Curso","UF do Curso":"Estado",
                        "Inscritos":"Concluintes Inscritos","Participantes":"Concluintes Participantes"})
df["Categoria Administrativa"]= ""  #Adciona uma coluna nova, em branco
df["Modalidade de Ensino"] = "" #Adciona uma coluna nova, em branco

#Print teste
#print(df)
print(df.info())

#Reordenar as colunas na ordem desejada
cols = list(df.columns) #Cria uma lista com o nome das colunas de Df
cols = cols[:5]+cols[11:]+cols[5:11] #Concatena as colunas da seguinte maneira: 0-4 + 12,12 + 5-10

#Print para teste
#print(cols)

df = df[cols]  #Redefine a ordem das colunas a partir da ordem definida acima.

#Print para teste
#print(df.info())

#Define os cursos a serem analisados
MatBac = df[df["Área de Avaliação"] == "MATEMÁTICA (BACHARELADO)"] #Cria uma nova base com os Curso 1
MatLic = df[df["Área de Avaliação"] == "MATEMÁTICA (LICENCIATURA)"] #Cria uma nova base com os Curso 2
MAT = pd.concat([MatBac,MatLic],axis=0).reset_index(drop=True) #Concatena as duas bases criadas acima
# Opção reset_index(drop=True) "reseta" o indece

#Print teste
#print(MAT.info())
#print(MAT["Conceito Enade (Contínuo)"].value_counts().sort_index())
#print(MAT["Conceito Enade (Faixa)"].value_counts())

MAT["Conceito Enade (Faixa)"] = pd.to_numeric(MAT["Conceito Enade (Faixa)"],errors="coerce") #Ajusta a coluna Conceito Enade (Faixa) para número
# OBS:: No comando acima, alguns valores não são nuḿericos, então, o argmento "errors="coerce"" faz com que estes se tornem null
MAT["Conceito Enade (Faixa)"] = MAT["Conceito Enade (Faixa)"].fillna(0) #Troca os campos nulos da coluna Conceito Enade por 0
#MAT["Conceito Enade (Contínuo)"] = pd.to_numeric(MAT["Conceito Enade (Contínuo)"].str.replace(",","."),errors="coerce")
#Na linha de cima, trocamos os pontos da coluna por pontos, antes de convertermos para numéricos
MAT["Conceito Enade (Contínuo)"] = MAT["Conceito Enade (Contínuo)"].fillna(0)

#Print teste
print(MAT.info())
print(MAT["Conceito Enade (Contínuo)"].value_counts().sort_index())
print(MAT["Conceito Enade (Faixa)"].value_counts().sort_index())


#Exporta o arquivo em CSV e xlsx
MAT.to_csv("enade_matematica_2014.csv",index=False)
MAT.to_excel("enade_matematica_2014.xlsx",index=False)
