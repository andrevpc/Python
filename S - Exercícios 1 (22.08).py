# =============================================================================
# # 1. Tabuada do 13
# for i in range(1, 11):
#     n = 13*i
#     print(f"13 x {i} =",n)
#     i = i+1
# =============================================================================

# =============================================================================
# # 2. Lista de 5 e ler menor valor
# lista = []
# for i in range(1,6):
#     n = int(input("Insira um número: "))
#     lista.append(n)
#     lista.sort()
# print(lista[0])
# =============================================================================

# =============================================================================
# # 3. True se estiver ordenada
# lista = []
# for i in range(1,6):
#     n = int(input("Insira um número: "))
#     lista.append(n)
#     listac = lista[:]
# listac.sort()
# if lista == listac:
#     print("Sim.!",lista)
# else:
#     print("Não está em ordem")
# =============================================================================

# =============================================================================
# # 4. Ordem decrescente de 500 à 10
# for i in range(500,9,-1):
#     print (i)
# 
# 5. Digitar 10 n e mostrar quantidade de 10 à 50
# lista = []
# for i in range(1,11):
#     n = int(input("Insira um número: "))
#     if n >10 and n < 50:
#         lista.append(n)
# lista.sort()
# print(lista)
# =============================================================================

# =============================================================================
# # 6. Sexo e idade (Média)
# m=0
# mm=0
# mf=0
# mas=0
# f=0
# for i in range(1,4):
#     n=int(input("Insira sua idade: "))
#     s=input("Insira o seu sexo (masculino ou feminino): ")
#     m=m+n
#     if s.lower() == "masculino":
#         mm = mm+n
#         mas=mas+1
#     if s.lower() == "feminino":
#         mf=mf+n
#         f=f+1
# print("Média feminina: ",mf/f)
# print("Média masculina: ",mm/mas)
# print("Média total: ",m/(f+mas))
# =============================================================================
