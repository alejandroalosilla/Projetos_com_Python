# Lógica de programação

# Passo 0 - Entender o desafio que você quer resolver

# Passo 1 - Percorrer todos os arquivos da pasta base de dados (Pasta Vendas)
import os # Importante biblioteca os (Mecher com arquivos do PC)
import pandas as pd # importando biblioteca pandas e apelidando como "pd" (Mecher com base de dados)

lista_arquivo = os.listdir("/content/drive/MyDrive/Curso Básico de Python/Vendas") # Lista o diretório
tabela_total = pd.DataFrame() # Cria uma tabela vazia (de início)

# Passo 2 - Importar as bases de dados de vendas
for arquivo in lista_arquivo:
  # Se tem "Vendas" no nome do arquivo, então
  if 'vendas' in arquivo.lower():
    # Importar o arquivo
    tabela = pd.read_csv(f"/content/drive/MyDrive/Curso Básico de Python/Vendas/{arquivo}")
    tabela_total = pd.concat([tabela]) # adicionando cada arquivo a tabela vazia (tabela_total)

# Passo 3 - Tratar / Compilar as bases de dados
display(tabela_total)

# Passo 4 - Calcular o produto mais vendido (em quantidade)

# Passo 5 - Calcular o produto que mais faturou (em faturamento)

# Passo 6 - Calcular a loja / cidade que mais vendeu (em faturamento)