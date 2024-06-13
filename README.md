*Análise de Vendas*

Descrição
Este script em Python tem como objetivo realizar a análise dos dados de vendas de uma loja, utilizando as bibliotecas pandas, matplotlib, e seaborn. O código carrega os dados de duas planilhas Excel: uma contendo informações dos produtos (Produtos.xlsx) e outra contendo os detalhes das vendas (Vendas.xlsx). A seguir, ele processa e visualiza os dados para extrair insights importantes, como o total vendido de cada produto, o lucro total, a margem de lucro percentual e os dias com maior número de vendas.

*Funcionalidades*

Carregamento dos Dados:
*Utiliza pandas para ler os arquivos Excel Produtos.xlsx e Vendas.xlsx.*
Processamento de Dados:
Agrupa os dados de vendas por SKU para calcular a quantidade total vendida de cada produto.
Merge dos dados de vendas com os detalhes dos produtos utilizando o SKU como chave.
Cálculo de Indicadores:
Lucro Total: Calcula o lucro total de cada produto como Quantidade Vendida * (Preço Unitário - Custo Unitário).
Margem de Lucro (%): Calcula a margem de lucro percentual para cada produto.
Análise de Dias de Vendas:
Agrupa as vendas por data e calcula a quantidade total vendida em cada dia.
Ordena os dias por quantidade de vendas em ordem decrescente para identificar os dias com maior número de vendas.
Visualização dos Dados:
Gera gráficos de barras utilizando seaborn para:
Total vendido de cada produto.
Margem de lucro percentual de cada produto.
Dias com maior número de vendas.



