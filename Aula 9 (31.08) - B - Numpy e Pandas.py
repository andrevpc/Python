# =============================================================================
# # Desafios
# =============================================================================

# =============================================================================
# # Exercício 1 - Vetor com números pares (20 a 90)
# import numpy as np
# 
# array=np.arange(20,90,2)
# print(array)
# # [20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66
# #  68 70 72 74 76 78 80 82 84 86 88]
# =============================================================================

# =============================================================================
# # Exercício 2 - Programa que soma todos os elementos de um vetor
# import numpy as np
# 
# array=np.arange(0,10,1)
# print(array)
# 
# print(array.mean()*len(array))
# # [0 1 2 3 4 5 6 7 8 9]
# # 45.0
# =============================================================================

# =============================================================================
# # Exercício 3 - Programa que calcule a soma de uma matriz
# import numpy as np
# 
# matriz=np.arange(0,9,1).reshape((3,3))
# print(matriz)
# ixj = matriz.shape
# print(ixj)
# print(matriz.mean()*(ixj[0]*ixj[1]))
# # [[0 1 2]
# #  [3 4 5]
# #  [6 7 8]]
# # (3, 3)
# # 36.0
# =============================================================================

# =============================================================================
# # Exercício 4 - Matriz aleatória (0 até 1)
# import numpy as np
# 
# matriz=np.random.rand(3,3)
# print(matriz)
# # [[0.78153598 0.90704006 0.64561817]
# #  [0.80045639 0.27748416 0.18978689]
# #  [0.36575216 0.52335449 0.03098276]]
# =============================================================================

# =============================================================================
# # Exercício 5 - Produto matricial (A6x6*B6x6) com números aleatórios
# # -1 até 1
# import numpy as np
# 
# A=np.random.randint(-1,1,36).reshape((6,6))
# print(A)
# B=np.random.randint(-1,1,36).reshape((6,6))
# print(B)
# print(np.dot(A,B))
# # [[-1  0  0  0 -1  0]
# #  [-1  0  0  0 -1  0]
# #  [ 0  0 -1  0  0  0]
# #  [ 0 -1 -1 -1  0  0]
# #  [-1  0  0 -1 -1  0]
# #  [-1  0  0 -1  0 -1]]
# # [[ 0 -1  0  0 -1 -1]
# #  [ 0 -1  0 -1  0 -1]
# #  [-1  0  0  0 -1 -1]
# #  [-1 -1  0  0 -1  0]
# #  [-1  0  0  0 -1  0]
# #  [-1  0  0 -1  0  0]]
# # [[1 1 0 0 2 1]
# #  [1 1 0 0 2 1]
# #  [1 0 0 0 1 1]
# #  [2 2 0 1 2 2]
# #  [2 2 0 0 3 1]
# #  [2 2 0 1 2 1]]
# =============================================================================

# =============================================================================
# # Exercício 6 - Produto de AnxmBmxp sem usar dot, só para comparar resposta
# import numpy as np
# 
# n = int(input("Qual o números de linha da sua matriz 1: "))
# m = int(input("Qual o números de colunas da sua matriz 1 e linhas da 2: "))
# p = int(input("Qual o números de colunas da sua matriz 2: "))
# A=np.random.randint(0,10,(n*m)).reshape((n,m))
# print(A)
# B=np.random.randint(0,10,(m*p)).reshape((m,p))
# print(B)
# print(np.dot(A, B))
# lista = []
# for linha in range(n):
#     for coluna in range(p):
#         soma = 0
#         for k in range(m):
#             soma = soma + A[linha][k] * B[k][coluna]
#         lista.append(soma)
# produto = np.array(lista).reshape(n,p)
# print('\n',produto)
# # Qual o números de linha da sua matriz 1: 2
# 
# # Qual o números de colunas da sua matriz 1 e linhas da 2: 3
# 
# # Qual o números de colunas da sua matriz 2: 1
# # [[2 2 1]
# #  [2 9 9]]
# # [[1]
# #  [0]
# #  [5]]
# # [[ 7]
# #  [47]]
# 
# #  [[ 7]
# #  [47]]
# =============================================================================

# =============================================================================
# # Exercício 7 - Vetor em °C (valores de 0 a 90) com 20 valores e outro em Fahrenheit
# import numpy as np
# 
# c = np.random.randint(0, 90, 20)
# f = c*(9/5)+32
# print(c)
# print(f)
# # [70 27 80  0 10 80 48 28 88 20 40  4 64 10 43 62 37 29 32 52]
# # [158.   80.6 176.   32.   50.  176.  118.4  82.4 190.4  68.  104.   39.2
# #  147.2  50.  109.4 143.6  98.6  84.2  89.6 125.6]
# =============================================================================
 
# =============================================================================
# # Exercício 8 - Verificar se A é simétrica (A=At)
# import numpy as np
# 
# A=np.array([5,1,2,1,6,3,2,3,8]).reshape(3,3)
# print(A)
# print(A.shape)
# 
# verificacao = 1
# for linha in range(A.shape[0]):
#     for coluna in range(A.shape[1]):
#         if A[linha,coluna] != A[coluna,linha]:
#             verificacao = 0
#             
# if verificacao == 1:
#     print("Simetrico")
# else:
#     print("Não simetrico")
# # [[5 1 2]
# #  [1 6 3]
# #  [2 3 8]]
# # (3, 3)
# # Simetrico
# # [[ True  True  True]
# #  [ True  True  True]
# #  [ True  True  True]]
# =============================================================================

# =============================================================================
# # Exercício 9 - Programa que resolve sistemas de equação com N equações (Ax = b)
# # e verificar se esta certo
# import numpy as np
# 
# N = int(input("Selecione o número de icognitas: "))
# 
# A = np.floor(100*np.random.rand(N,N))
# B = np.floor(100*np.random.rand(N,1))
# print(A)
# Ai = np.linalg.inv(A)
# print(Ai)
# X = Ai.dot(B)
# B2 = A.dot(X)
# print(X)
# 
# if np.array_equal(np.round(B,2),np.round(B2,2)) == True:
#   print("Calculo certo")
# =============================================================================
 
# =============================================================================
# # Exercício 10 - Programa que crie um arquivo (seno.txt) com duas colunas,
# # primeira com 100 valores entre 0 e 2pi e a segunda com o seno dos valores
# # com 6 casas decimais
# import numpy as np
# import math
# 
# numeros = list(2*math.pi*np.random.random(100))
# senos = []
# 
# for i in range(100):
#     senos.append(math.sin(numeros[i]))
#     
# planilha = np.array([numeros,senos])
# planilha = np.transpose(planilha)
# np.savetxt("seno.txt,",planilha,fmt="%.6f")
# =============================================================================

# =============================================================================
# # Exercício 11 - Ler o arquivo txt e armazenar a primeira coluna
# # no vetor x e a segunda no vetor f
# import numpy as np
# 
# seno = np.loadtxt("seno.txt")
# x = np.zeros(seno.shape[1])
# f = np.zeros(seno.shape[1])
# seno = np.transpose(seno)
# x = seno[0]
# f = seno[1]
# =============================================================================

# =============================================================================
# # Usando a biblioteca pandas
# # Para pegar tabelas e ler:
# import pandas as pd
# 
# titanic = pd.read_csv("titanic.csv", sep=',')
# print(titanic)
# =============================================================================

# =============================================================================
# # Para ler apenas uma coluna
# print(titanic['survived'])
# 
# # Duas
# print(titanic[['survived', "age"]])
# 
# # Se é igual a zero (True ou False)
# print(titanic['survived'] == 0)
# 
# # Para saber quantas linhas e colunas
# print(titanic.shape)
# =============================================================================

# =============================================================================
# # Exercício 1 - Retornar todas as colunas menos a ultima
# import pandas as pd
# 
# titanic = pd.read_csv("titanic.csv", sep=',')
# print(titanic.iloc[:,:-1])
# =============================================================================
