# Lógica de programação

# Passo 0 - Entender o desafio que você quer resolver

# Passo 1 - Percorrer todos os arquivos da pasta base de dados (Pasta Vendas)
import os

lista_arquivo = os.listdir("/content/drive/MyDrive/Curso Básico de Python/Vendas")

# Passo 2 - Importar as bases de dados de vendas
for arquivo in lista_arquivo:
  # Se tem "Vendas" no nome do arquivo, então
  if 'vendas' in arquivo.lower():
    print(f"/content/drive/MyDrive/Curso Básico de Python/Vendas/{arquivo}")
  # Importar o arquivo
  
# Passo 3 - Tratar / Compilar as bases de dados

# Passo 4 - Calcular o produto mais vendido (em quantidade)

# Passo 5 - Calcular o produto que mais faturou (em faturamento)

# Passo 6 - Calcular a loja / cidade que mais vendeu (em faturamento)