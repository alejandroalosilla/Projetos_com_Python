# Passo 1 - Percorrer todos os arquivos da pasta base de dados (Pasta Vendas)
import os # Importar biblioteca os (Mecher com arquivos do PC)
import pandas as pd # importando biblioteca pandas e apelidando como "pd" (Mecher com base de dados)
import plotly.express as px

lista_arquivo = os.listdir("/content/drive/MyDrive/Curso Básico de Python/Vendas") # Lista o diretório
tabela_total = pd.DataFrame() # Cria uma tabela vazia (de início)

# Passo 2 - Importar as bases de dados de vendas
for arquivo in lista_arquivo:
  # Se tem "Vendas" no nome do arquivo, então
  if 'vendas' in arquivo.lower():
    # Importar o arquivo
    tabela = pd.read_csv(f"/content/drive/MyDrive/Curso Básico de Python/Vendas/{arquivo}")
    tabela_total = pd.concat([tabela_total, tabela]) # adicionando cada arquivo a tabela vazia (tabela_total)

# Passo 3 - Tratar / Compilar as bases de dados
print('Tabela Unificada: ')
print(tabela_total)

# Passo 4 - Calcular o produto mais vendido (em quantidade)
if 'Produto' in tabela_total.columns:
  tabela_produtos = tabela_total.groupby('Produto')['Quantidade Vendida'].sum().reset_index() # Agrupando os elementos da tabela com base na coluna "Produto" e somando as quantidades
  tabela_produtos = tabela_produtos.sort_values('Quantidade Vendida', ascending=False)
  print('\nCalcular o produto mais vendido:')
  print(tabela_produtos)
else:
  print("A coluna 'Produto' não existe na tabela.")

# Passo 5 - Calcular o produto que mais faturou (em faturamento)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto')['Faturamento'].sum().reset_index()
tabela_faturamento = tabela_faturamento.sort_values('Faturamento', ascending=False)
print('\nCalcular o produto que mais faturou: ')
print(tabela_faturamento)
# Passo 6 - Calcular a loja / cidade que mais vendeu (em faturamento)
tabela_lojas = tabela_total.groupby('Loja')['Faturamento'].sum().reset_index()
tabela_lojas = tabela_lojas.sort_values('Faturamento', ascending=False)
print('\nLoja que mais vendeu: ')
print(tabela_lojas)

# Passo 7 - Criar um gráfico/dashboard

grafico = px.bar(tabela_lojas, x='Loja', y='Faturamento')
print('\nGráfico de Faturamento das Lojas: ')
grafico.show()
