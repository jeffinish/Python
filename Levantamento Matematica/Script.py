# Arquivo para analisar arquivos do enade pra Matemática
import pandas as pd #Importa o Panda para trabalhar com o arquivo Excel
import plotly.express as px #Importa o Plotly para fazer gráficos e histogramas
from googlesearch import search #Importa a API do google pra procurar

pd.set_option("display.max_rows",10) #Seta o máximo de linhas para ser exibida
pd.set_option("display.max_columns",5) #Seta o máximmo de colunas para ser exibida

df = pd.read_csv("resultados_conceito_enade_2017.csv") #Abre o arquivo xlxs
dr = df.drop(["Ano","Código da IES","Sigla da IES",
            "Nota Bruta - FG","Nota Padronizada - FG", "Nota Bruta - CE", "Nota Padronizada - CE",
            "Observação"]
            ,axis=1) #Dropa algumas colunas

#Print teste
#print(dr)
#print(dr.info())

#Define os cursos a serem analisados
curso1 = "MATEMÁTICA (BACHARELADO)"  #Define o primeiro curso a ser avaliado
curso2 = "MATEMÁTICA (LICENCIATURA)" #Define o segundo curso a ser avaliado
MatBac = dr[dr["Área de Avaliação"] == curso1] #Cria uma nova base com os Curso 1
MatLic = dr[dr["Área de Avaliação"] == curso2] #Cria uma nova base com os Curso 2
MAT = pd.concat([MatBac,MatLic],axis=0).reset_index(drop=True) #Concatena as duas bases criadas acima
# Opção reset_index(drop=True) "reseta" o indece

#Print teste
#print(MAT.info())
print(MAT["Conceito Enade (Contínuo)"].value_counts().sort_index())
#print(MAT["Conceito Enade (Faixa)"].value_counts())

MAT["Conceito Enade (Faixa)"] = pd.to_numeric(MAT["Conceito Enade (Faixa)"],errors="coerce") #Ajusta a coluna Conceito Enade (Faixa) para número
# OBS:: No comando acima, alguns valores não são nuḿericos, então, o argmento "errors="coerce"" faz com que estes se tornem null
MAT["Conceito Enade (Faixa)"] = MAT["Conceito Enade (Faixa)"].fillna(0) #Troca os campos nulos da coluna Conceito Enade por 0
MAT["Conceito Enade (Contínuo)"] = pd.to_numeric(MAT["Conceito Enade (Contínuo)"].str.replace(",","."),errors="coerce")
#Na linha de cima, trocamos os pontos da coluna por pontos, antes de convertermos para numéricos
MAT["Conceito Enade (Contínuo)"] = MAT["Conceito Enade (Contínuo)"].fillna(0)
#Print teste
#print(MAT.info())
print(MAT["Conceito Enade (Contínuo)"].value_counts().sort_index())
#print(MAT["Conceito Enade (Faixa)"].value_counts())

#Aqui começa uma gambiarra para ober os X estados com maior número de cursos de matemática
#X = (MAT["Sigla da UF"].value_counts().to_frame("Quantidade").reset_index())

#Print teste
#print(X)
#Melhores = 5
#print(X["index"][:1])

#Printa os 5 melhores estados
#for i in range(0,Melhores):
#    print(X["index"][i])
#Printa uma frasezinha falando dos estados com o estado e o número de cursos
#for i in range(0,Melhores):
#    print("{0} é o estado em {1} lugar em quantidade de cursos com {2} cursos".format(X["index"][i],i+1,X["Quantidade"][i]))

#Começa a Análise apenas dos resultados

#Print teste
#IES = MAT["Nome da IES"] #Define uma nova variáveil que guarda só o nome das IES

#Print teste
#print(IES.value_counts()) ##Confere quantas IES existem

#IES = IES.drop_duplicates().reset_index(drop=True) #Dropa as IES que aperecem duplicadas

#Print teste
#print(IES.value_counts()) #Confere se todo mundo aparece só uma vez.
#print(IES.head())

#fig = px.histogram(MAT,x=MAT["Conceito Enade (Faixa)"],color="Área de Avaliação")
#fig.show()

#Print teste
#print(MAT.info())
#print(MAT["Conceito Enade (Contínuo)"])

#Exporta o arquivo em CSV
MAT.to_csv("enade_matematica_2017.csv",index=False)



#Aqui começa a parte da busca no google
#num_page = 3 #Define o número de resultados que o google vai retornar
#site1 = search(IES[1]+"Matemática",num_results=3)
#site2 = search(IES[2]+"Matemática",num_results=3)
#print(site1)
#print(site2)
#sites = pd.DataFrame(site1,columns=["Resultado1","Resultado2","Resultado3","Resultado4"])
#print(sites)
#sites = pd.DataFrame(columns=["Resultado1","Resultado2","Resultado3","Resultado4"])
#print(sites)
#search_results = pd.DataFrame(search(IES[4]+"Matemática",num_results=3),columns=["Resultado1","Resultado2","Resultado3","Resultado4"])
#print(search_results)
#for facul in IES:
    #search_results = pd.DataFrame(search(facul+"Matemática",num_results=3),columns=["Resultado1","Resultado2","Resultado3","Resultado4"])
    #pd.concat([sites,search_results],axis=0,ignore_index=True)
#print(sites.head())
