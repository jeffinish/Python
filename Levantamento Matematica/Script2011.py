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

#Ano - 2011
df = pd.read_excel("resultados_conceito_enade_2011.xls") #Abre o arquivo xlxs
df = df.drop(["Sigla IES","Código Área Agrupamento","Código UF","Organização Acadêmica",
                "Número Cursos Unidade","Código Município",
                "Média FG Conc","Média CE Conc","Nota Enem Ingressantes",
                "Nota IDD","Proporção de respostas sobre infraestrutura","Nota de Infraestrutura",
                'Número Ingressantes Inscritos','Número Ingressantes Participantes no  Enem',
                'Proporção de respostas sobre plano ensino','Nota de Organização Pedagógica',
                'Número docentes','Proporção Docentes Mestres','Nota Mestrado','Proporção Docentes Doutores',
                'Nota Doutorado','Proporção Docentes Parc Integral','Nota Regime','CPC Contínuo','CPC Faixa'],axis=1)
df["Modalidade de Ensino"] = "" #Adciona uma coluna nova, em branco
cols = list(df.columns) #Coloca o nome das colunas na variável cols
#Print teste
#print(df)
print(cols)
print(df.info())
