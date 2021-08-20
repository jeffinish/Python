import pandas as pd
df = pd.read_excel(r'/home/jefferson/OneDrive/Pessoal/Python/Intensivao_Python/Vendas - Dez.xlsx')
print(df)
faturamento = df['Valor Final'].sum()
print(faturamento)
