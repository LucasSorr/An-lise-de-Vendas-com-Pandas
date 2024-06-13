import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados da planilha de produtos
produtos_df = pd.read_excel('Produtos.xlsx')

# Carregar dados da planilha de vendas
vendas_df = pd.read_excel('Vendas.xlsx')

# Agrupar vendas pelo SKU e calcular o total vendido de cada produto
total_vendido = vendas_df.groupby('SKU')['Quantidade'].sum().reset_index()

# Relacionar com os dados dos produtos usando o SKU
dados_completos = pd.merge(total_vendido, produtos_df, on='SKU')

# Calcular o lucro total de cada produto
dados_completos['Lucro Total'] = dados_completos['Quantidade'] * (dados_completos['Preço Unitario'] - dados_completos['Custo Unitario'])

# Calcular a margem de lucro em porcentagem
dados_completos['Margem de Lucro (%)'] = ((dados_completos['Preço Unitario'] - dados_completos['Custo Unitario']) / dados_completos['Preço Unitario']) * 100

# Identificar os dias que mais venderam
vendas_por_dia = vendas_df.groupby('Data da venda')['Quantidade'].sum().reset_index()

# Ordenar por quantidade de vendas decrescente para identificar os dias de maior venda
dias_mais_vendidos = vendas_por_dia.sort_values(by='Quantidade', ascending=False)

# Ordenar dados completos por quantidade vendida para facilitar o ajuste dos gráficos
dados_completos = dados_completos.sort_values(by='Quantidade', ascending=False)

# Gerar gráfico para representar o total vendido de cada produto
plt.figure(figsize=(12, 8))
sns.barplot(x='Produto', y='Quantidade', data=dados_completos, palette='viridis')
plt.title('Total Vendido de Cada Produto')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Gerar gráfico para representar a margem de lucro em porcentagem de cada produto
plt.figure(figsize=(12, 8))
sns.barplot(x='Produto', y='Margem de Lucro (%)', data=dados_completos, palette='magma')
plt.title('Margem de Lucro (%) de Cada Produto')
plt.xlabel('Produto')
plt.ylabel('Margem de Lucro (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Gerar gráfico para representar os dias de maior venda
plt.figure(figsize=(12, 8))
sns.barplot(x='Data da venda', y='Quantidade', data=dias_mais_vendidos, palette='rocket')
plt.title('Dias com Maior Número de Vendas')
plt.xlabel('Data da Venda')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()