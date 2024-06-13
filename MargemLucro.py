import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#(CRIAÇÃO DE UM GRAFÍCO COM O CALCULO DA MARGEM DE LUCRO DE CADA TIPO DE PRODUTO)

# Carregar dados do Excel 
df = pd.read_excel('Produtos.xlsx')
# Calcular margem de lucro (%)
df['Margem de Lucro (%)'] = ((df['Preço Unitario'] - df['Custo Unitario']) / df['Custo Unitario']) * 100
# Calcular média da margem de lucro por Tipo do Produto
media_margem_lucro = df.groupby('Tipo do Produto')['Margem de Lucro (%)'].mean().reset_index()
# Exibir a média da margem de lucro por Tipo do Produto
print("Média da Margem de Lucro por Tipo do Produto:")
print(media_margem_lucro)
# Plotar um gráfico de barras para visualizar a média da margem de lucro por Tipo do Produto
plt.figure(figsize=(10, 6))
sns.barplot(x='Tipo do Produto', y='Margem de Lucro (%)', data=media_margem_lucro)
plt.title('Média da Margem de Lucro por Tipo do Produto')
plt.xlabel('Tipo do Produto')
plt.ylabel('Média da Margem de Lucro (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


