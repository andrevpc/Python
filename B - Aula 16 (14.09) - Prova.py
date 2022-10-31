# =============================================================================
# # Exercício 1
# a = float(input("Digite o lado A: "))
# b = float(input("Digite o lado B: "))
# c = float(input("Digite o lado C: "))
# if abs(b-c)<a<b+c and abs(a-c)<b<a+c and abs(a-b)<c<a+b:
#     print("É um triangulo equilatero" if (a==b==c) else ("É um triangulo isósceles" if (a==b or b==c) else "É um triangulo escaleno"))
# else:
#     print("Não é um triangulo")
# =============================================================================

# =============================================================================
# # Exercício 2
# dic = {"Palmeiras":30, "Corinthians":24, "Fluminense":17, "Vasco da Gama":12}
# nr = int(input("Insira o número de rodadas: "))
# pflu = 0
# pcor = 0
# pvas = 0
# ppal = 0
# b = 0
#     
# for i in range(nr):
#     flu = int(input(print('''Resultado da partida para Fluminense
#           1 - Vitória
#           2 - Derrota
#           3 - Empate''')))
#     cor = int(input(print('''Resultado da partida para Corinthians
#           1 - Vitória
#           2 - Derrota
#           3 - Empate''')))
#     vas = int(input(print('''Resultado da partida para Flamengo
#           1 - Vitória
#           2 - Derrota
#           3 - Empate''')))
#     pal = int(input(print('''Resultado da partida para Palmeiras
#           1 - Vitória
#           2 - Derrota
#           3 - Empate''')))
#     if pal == 1:
#         ppal += 3
#     elif pal == 2:
#         ppal += 0
#     elif pal == 3:
#         ppal += 1
#     else:
#         ("Valor invalido")
#         
#     if flu == 1:
#         pflu += 3
#     elif flu == 2:
#         pflu += 0
#     elif flu == 3:
#         pflu += 1
#     else:
#         ("Valor invalido")
#         
#     if cor == 1:
#         pcor += 3
#     elif cor == 2:
#         pcor += 0
#     elif cor == 3:
#         pcor += 1
#     else:
#         ("Valor invalido")
#         
#     if vas == 1:
#         pvas += 3
#     elif vas == 2:
#         pvas += 0
#     elif vas == 3:
#         pvas += 1
#     else:
#         ("Valor invalido")
#     
# 
# dic["Palmeiras"] = dic["Palmeiras"] + ppal
# dic["Corinthians"] = dic["Corinthians"] + pcor
# dic["Fluminense"] = dic["Fluminense"] + pflu
# dic["Vasco da Gama"] = dic["Vasco da Gama"] + pvas
# 
# print(f"O time com maior pontuação foi o {max(dic, key=dic.get)} com {dic[max(dic, key=dic.get)]}")
# =============================================================================

# =============================================================================
# # Exercício 3
# num = int(input("Insira um número maior que zero\n"))
# numstr = str(num)
# somaalg = 0
# try:
#     for i in range(len(numstr)):
#         somaalg += int(numstr[i])
#     print("A soma dos algarismos é igual a ", somaalg)
# except:
#     print("Número Inválido")
# =============================================================================

# =============================================================================
# # Exercício 4
# respostas = []
# gabarito = ["a","b","c","d","e","a","b","c","d","e"]
# erros = []
# nota = 0
# for i in range(10):
#     aux = input(f"Qual a resposta para a questão {i+1}?")
#     respostas.append(aux)
# for i in range(len(respostas)):
#     if respostas[i] == gabarito[i]:
#         nota += 1
#     else:
#         erros.append(i+1)
# print("Sua nota foi ", nota)
# print("Você errou as respostas: ", erros)
# =============================================================================

# =============================================================================
# # Exercício 5
# import random
# sorteado = random.randint(1,1000)
# lista3 = []
# for i in range(-3,4,1):
#     lista3.append(sorteado+i)   
# aux = 0
# while 1:
#     num = int(input("Tente acertar o número sorteado: "))
#     if num == sorteado:
#         print("Parabéns você acertou!! O número é ", sorteado)
#         break
#     elif num in lista3:
#         print("Quase!!")
#     elif num > sorteado:
#         print("Muito alto")
#     elif num < sorteado:
#         print("Muito baixo")
#     aux += 1
# print(f"Foram necessárias {aux+1} tentativas")
# =============================================================================

# =============================================================================
# # Exercício 6
# senha = input("Insira a senha para ser codificada\n")
# listase = list(senha)
# listabin = []
# 
# for i in range(len(listase)):
#     print(int(listase[i]))
#     listabin.append(temp = "{0:b}".format(int(listase[i])))
#         
# print(listabin)
# 
# def codificacao(senha, listase):
#     for i in listase:
#         print(int(listase[i]))
#         listabin.append(temp = "{0:b}".format(int(listase[i])))
#             
#     print(listabin)
# =============================================================================

# =============================================================================
# # Exercício 7
# lista=[]
# arquivo = open("arquivo.txt", "w")
# arquivo.write('''André
# 8.9
# 9.7
# Peterson
# 10
# 9.8
# Kaiky
# 9.5
# 8.5
# Bruno
# 9.9
# 9.3''')
# arquivo.close()
# 
# arquivo = open("arquivo.txt", "r")
# for linha in arquivo:
#     lista.append(linha.rstrip('\n'))
#     
# nome = input("Selecione um aluno: André, Peterson, Kaiky e Bruno\n")
# ind = lista.index(nome)
# print(f"A média do {nome} é {(float(lista[ind+1]) + float(lista[ind+2]))/2}")
# =============================================================================

# Exercício 8
import pandas as pd
import matplotlib.pyplot as plt

netflix = pd.read_csv("netflix_titles.csv", sep=',')
netflix = netflix.dropna()


netflixbr = netflix[(netflix["country"] == "Brazil")]
netflixbr = netflixbr[netflixbr["duration"].str.contains("min")]
netflixbr = netflixbr.reset_index()
netflixbr["duration"]= netflixbr[netflixbr["duration"].str.replace(" min", "")]
netflixbr = netflixbr.sort_values([int(netflixbr["duration"])], axis=0, ascending=True, inplace=True)
netflixbr = netflixbr.head()


netflix = netflix[((netflix["country"] == "United States") & ((netflix["release_year"]==2015) | (netflix["release_year"]==2016) | (netflix["release_year"]==2017) | (netflix["release_year"]==2018) | (netflix["release_year"]==2019) | (netflix["release_year"]==2020)))]
        
a2015 = netflix.release_year[netflix["release_year"] == 2015].count()
a2016 = netflix.release_year[netflix["release_year"] == 2016].count()
a2017 = netflix.release_year[netflix["release_year"] == 2017].count()
a2018 = netflix.release_year[netflix["release_year"] == 2018].count()
a2019 = netflix.release_year[netflix["release_year"] == 2019].count()
a2020 = netflix.release_year[netflix["release_year"] == 2020].count()

plt.bar(("2015", "2016", "2017", "2018", "2019", "2020"), (a2015,a2016,a2017,a2018,a2019,a2020))

# =============================================================================
# # Exercício 9
# import numpy as np
# 
# array = np.random.randint(1,10,(5,5)) # Criou a matriz 5 por 5 com números inteiros aleatórios de 1 à 10
# 
# print('\n', array)
# 
# condition = (array%2 != 0) # Criou uma condição para ver quem é impar
# array[condition] = array[condition]**2 # Elevou todos os impares ao quadrado
# 
# print("\n", array)
# =============================================================================
