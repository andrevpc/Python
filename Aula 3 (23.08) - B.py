# =============================================================================
# # Calculadora com área
# while 1:
#     C1 = int(input("""Qual o estilo?
#                    Calculadora: 1
#                    Área do quadrado: 2
#                    """))
# 
#     if C1 == 1:
#             N1 = int(input("Selecione o primeiro número: "))
#             N2 = int(input("Selecione o segundo número: "))
#             op = int(input("""
#                    1 - Soma
#                    2- Subtração
#                    3- Multiplicação
#                    4- Divisão
#                    0- Sair
#                    Escolha a operação: """))
#             if op == 0:
#                 break
#             elif op == 1:
#                 print(N1 +N2)
#             elif op == 2:
#                 print(N1 - N2)
#             elif op == 3:
#                 print(N1 * N2)
#             elif op == 4:
#                 print(N1 / N2)
#             else:
#                 print("Insira uma operação válida")
#     
#     if C1 == 2:
#         Q1 = int(input("Selecione o primeiro lado: "))
#         Q2 = int(input("Selecione o segundo lado: "))
#         print("A área dá: ",Q1*Q2)
# =============================================================================

# =============================================================================
# # Exercício 5 - Números pares de 1 a 30
# for i in range(31):
#     if i%2 == 0:
#         print(i)
# =============================================================================

# =============================================================================
# # Exercício 6 - Tabuleiro
# n=int(input("Selecione o tamanho do tabuleiro:" ))
# for i in range(n):
#     for j in range(n):
#         print("x", end=" ")
#     print("\n", end="")
# =============================================================================

# =============================================================================
# # Exercício 7 - Série Finonacci
# n = int(input("Selecione o número: "))
# primeiro = 0
# segundo = 1
# for i in range(n):
#     print(primeiro)
#     primeiro = primeiro + segundo
#     segundo = primeiro - segundo
# =============================================================================

# Nova aula

# =============================================================================
# # Exercício 1 - par ou impar com a maquina
# import random
# recorde = 0
# print("Seu recorde é: ",recorde)
# while 1:
#     e_usuario = input("par ou impar: ")
#     n_usuario = int(input("Escolha um número: "))
#     n_computador = (random.randint(0,10))
#     print("Número do computador: ", n_computador)
#     
#     if e_usuario.lower() == "par":
#         if (n_usuario+n_computador)%2 == 0:
#             print("Você Ganhou!")
#             recorde = recorde +1
#         elif (n_usuario+n_computador)%2 != 0:
#             print("Você Perdeu!")
#             print("Seu recorde é: ",recorde)
#             break
#     elif e_usuario.lower() == "impar":
#         if (n_usuario+n_computador)%2 == 0:
#             print("Você Perdeu!")
#             print("Seu recorde é: ",recorde)
#             break
#         elif (n_usuario+n_computador)%2 != 0:
#             print("Você Ganhou!")
#             recorde = recorde + 1
# =============================================================================