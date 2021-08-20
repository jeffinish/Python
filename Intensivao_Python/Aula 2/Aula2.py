import pandas as pd
df = pd.read_csv("telecom_users.csv") #Le o arquivo em read_csv
df = df.drop(["Unnamed: 0"],axis=1) #Remove a coluna Unnamed: 0
df["TotalGasto"] = pd.to_numeric(df["TotalGasto"],errors="coerce") #Troca o tipo do dado Total gasto para numero
df = df.dropna(how="all",axis=1) #Remove colunas totalmente nulas
df = df.dropna() #Remove linhas que contenham pelo menos um valor nulo
print(df.info())
print(df)

print(df["Churn"].value_counts())
print(df["Churn"].value_counts(normalize=True).map("{:.1%}".format))
