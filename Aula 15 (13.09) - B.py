# =============================================================================
# # Resvisao
# =============================================================================

# =============================================================================
# # Exercício 1 - Crie uma tupla com 5 valores aleatórios de 0 a 9, mostre o maior
# # e menor valor, mostre quantas vezes aparece o número 5 e em qual posição está
# # o primeiro número 2
# import random
# 
# tupla = tuple((random.randint(1, 9) for i in range(5)))
# print(tupla)
# print(f"O maior valor é {max(tupla)} e o menor é {min(tupla)}")
# print("O número 5 aparece:",tupla.count(5), "vezes")
# print(f"O primeiro número 2 aparece no index: {tupla.index(2)}" if 2 in tupla else "O número não aparece")
# =============================================================================

# =============================================================================
# # Exercício 2 - Peça altura e peso e calcule o IMC, dê em qual parte ele se encaixa
# a = float(input("Insira a sua altura: "))
# p = float(input("Insira o seu peso: "))
# imc = p/a**2
# print(imc)
# print("Você está magro" if imc<18.6 else ("Você está normal" if 18.5<imc<25 else("Você está com sobrepeso"if 24.9<imc<30 else("Você está obeso" if 29.9<imc<40 else "Você está com obesidade grave"))))
# =============================================================================

# =============================================================================
# # Exercício 3 - Matheus cresce 2 cm por ano e tem 1.5 e José cresce 3 cm por ano e tem 1.1
# # em quanto tempo José será mais alto que Matheus
# m, j = 1.5, 1.1
# ano = 0
# while m > j:
#     m = m + 0.02
#     j = j + 0.03
#     ano = ano+1
# print(ano)
# m, j = 1.5, 1.1
# ano = 0
# while 1:
#     m = m + 0.02
#     j = j + 0.03
#     ano = ano+1
#     if j>m:
#         break
# print(ano)
# =============================================================================

# =============================================================================
# # Exercício 4 - Verifique se o ano que o usuario escolheu é bissexto
# ano = int(input("Insira um ano: "))
# print("O ano é bissexto" if (ano%4 == 0 and ano%100 != 0) or (ano%400 == 0) else "O ano não é bissexto")
# if (ano%4 == 0 and ano%100 != 0) or (ano%400 == 0):
#         print("O ano é bissexto")
# else:
#     print("O ano não é bissexto")
# 
# for ano in range(2025):
#     if (ano%4 == 0 and ano%100 != 0) or (ano%400 == 0):
#         print(ano)
# =============================================================================

# =============================================================================
# # Exercício 5 - Crie uma função que verifique se um número é um quadrado perfeito
# # n = int(input("Insira um número: "))
# # if (n**0.5).is_integer():
# #     print("É um quadrado perfeito")
# # else:
# #     print("Não é um quadrado perfeito")
#     
# print("É um quadrado perfeito" if (int(input("Insira um número: "))**0.5).is_integer() else "Não é um quadrado perfeito")
# =============================================================================

# =============================================================================
# # Exercício 5 - Receba o nome e altura de 5 pessoas e armazene em um dicionario
# # mostre o nome da pessoa mais alta e da mais baixa
# # nome = []
# # altura = []
# # for i in range (2):
# #     n = input("Digite seu nome: ")
# #     a = int(input("Digite sua altura: "))
# #     nome.append(n)
# #     altura.append(a)
# # dic = dict(zip(nome, altura))
# # print("O maior número é: ", max(dic, key=dic.get))
# # print("O menor número é: ", min(dic, key=dic.get))
# 
# nome = []
# altura = []
# dic = {}
# for i in range (2):
#     n = input("Digite seu nome: ")
#     a = int(input("Digite sua altura: "))
#     dic[n] = a
# print(dic)
# print("O maior número é: ", max(dic, key=dic.get))
# print("O menor número é: ", min(dic, key=dic.get))
# =============================================================================

