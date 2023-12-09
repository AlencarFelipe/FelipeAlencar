import pandas as pd
import matplotlib.pyplot as plt

# Lista de vendedores
ranking_vendas ={
    "Vendedores":["James Rodriguez","Marcelo","Luis Suarez","Lucas Moura", "Payet"],
    "Valor_Vendido":[10000.00, 5000.00,7800.00,5800.00, 6000.00],
    "Conversao_vendas":[2000, 4000,7000,9000,1000]   
}

# criar seu dataframe
df= pd.DataFrame(ranking_vendas)
print(df)

media_vendas = df['Valor_Vendido'].mean()
media_conversao= df['Conversao_vendas'].mean()
maximo_venda = df['Valor_Vendido'].max()
minimo_venda = df['Valor_Vendido'].min()

print(f"A media das vendas foi de: {media_vendas}")
print(f"A media de conversao foi de: {media_conversao}")
print(f"O maior valor vendido foi: {maximo_venda}")
print(f"O menor valor vendido foi: {minimo_venda}")

df.plot( x = 'Vendedores', y=['Valor_Vendido', 'Conversao_vendas'],
kind='bar' )

plt.title("Rankig de Vendas ")

plt.xlabel("Vendedores")
plt.ylabel("Venda")
plt.show()