# ctrl 1: coloca #
# ctrl 4: marca envolta

# =============================================================================
# # Exercício 2 - Contador com passo e parametros
# def contador(start, end, steps):
#     if end < start:
#         steps = steps*-1
#         for i in range(start, end-1, steps):
#             print(i)
#     else:
#         for i in range(start, end+1, steps):
#             print(i)
# 
# contador(1,20,1)
# contador(20,0,2)
# contador(0,105,5)
# contador(96,52,2)
# contador(3,41,1)
# contador(75,15,5)
# contador(390,39,10)
# inicio=int(input("Selecione o número inicial: "))
# fim=int(input("Selecione o número final: "))
# passo=int(input("Selecione os passo: "))
# contador(inicio, fim, passo)
# =============================================================================

# =============================================================================
# # Exercício 3 - Calculadora (Raiz, quadrado, inverso e fatorial)
# import math
# 
# def calculadora(valor):
#     return {"Raiz quadrada":math.sqrt(valor),"Quadrado":valor**2,"Inverso":1/valor,"Fatorial":math.factorial(valor)}
#     
# value = int(input("Digite um valor: "))
# resultado = calculadora(value)
# print(resultado)
# 
# 
# print(resultado["Quadrado"]/2)
# 
# =============================================================================
# =============================================================================
# # Exercício 4 - Lista ordenada com números aleatórios
# import random
# 
# def lista(limite_inferior,limite_superior,tamanho_lista):
#     listar = []
#     for i in range(tamanho_lista) :
#         listar.append(random.randint(limite_inferior,limite_superior))
#     print(listar)
#     for j in range(tamanho_lista):
#         for i in range(tamanho_lista - 1):
#             if listar[i] > listar[i+1]:
#                 auxiliar = listar[i]
#                 listar[i] = listar[i+1]
#                 listar[i+1] = auxiliar
#             
#     print(listar)
# 
# liminf = int(input("Insira o limite inferior: "))
# limsup = int(input("Insira o limite superior: "))
# tamlis = int(input("Insira o tamanho da lista: "))
# lista(liminf,limsup,tamlis)
# =============================================================================

# Nova aula

# =============================================================================
# # Exercício 7.1 - Calculadora cokm mensagem de erro
# while 1:
#     while 1:
#         try:
#             N1 = int(input("Selecione o primeiro número: "))
#             N2 = int(input("Selecione o segundo número: "))
#             break
#         except ValueError:
#             print("Erro no valor, insira outro")
#     op = int(input("""
#                    1 - Soma
#                    2- Subtração
#                    3- Multiplicação
#                    4- Divisão
#                    0- Sair
#                    Escolha a operação: """))
#     if op == 0:
#         break
#     elif op == 1:
#         print(N1 +N2)
#     elif op == 2:
#         print(N1 - N2)
#     elif op == 3:
#         print(N1 * N2)
#     elif op == 4:
#         try:
#             print(N1 / N2)
#         except ZeroDivisionError:
#             print("Impossível dividir po 0!")
#             pass
#             
#     else:
#         print("Insira uma operação válida")
# =============================================================================

# =============================================================================
# # Transferir informações para txt - o arquivo deve estar na mesma pasta
# # do .py (Para adicionar o texto, sem exclui-lo use "a" no lugar de "w"
# arquivo = open("arquivo.txt", "w")
# arquivo.write("Banana\n")
# arquivo.close()
# =============================================================================

# =============================================================================
# # ler informações para txt
# arquivo = open("arquivo.txt", "r")
# for linha in arquivo:
#     print(linha)
# =============================================================================

# =============================================================================
# # Exercício 7.2 - Ver quantas vezes uma certa palavra repete num .txt
# arquivo = open("arquivo.txt", "r")
# Ler = arquivo.read()
# print(Ler.count("Banana"))
# 
# # Ou
# 
# palavra = input("Digite uma palavra: ")
# quant = 0
# with open("arquivo.txt") as arquivo:
#     for linha in arquivo:
#         palavras = linha.strip().split()
#         if palavra in palavras:
#             quant += 1
# if quant > 0:
#     print(f"'{palavra}' apareceu {quant} vezes")
# else:
#     print(f"'{palavra} não apareceu")
# =============================================================================
