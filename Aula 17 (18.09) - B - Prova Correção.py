# =============================================================================
# # Exercício 1
# a,b,c = float(input("Digite o lado A: ")), float(input("Digite o lado B: ")), float(input("Digite o lado C: "))
# print(("É um triangulo equilatero" if (a==b==c) else ("É um triangulo isósceles" if (a==b or b==c) else "É um triangulo escaleno")) if (abs(b-c)<a<b+c and abs(a-c)<b<a+c and abs(a-b)<c<a+b) else "Não é um triangulo")
# =============================================================================

# =============================================================================
# # Exercício 2
# dic = {"Palmeiras":30, "Corinthians":24, "Fluminense":17, "Vasco da Gama":12}
# nr = int(input("Insira o número de rodadas: "))
# 
# def Pontos(time, ptime):
#     if time == 1:
#         dic[ptime] += 3
#     elif time == 2:
#         dic[ptime] += 0
#     elif time == 3:
#         dic[ptime] += 1
#     else:
#         ("Valor invalido")
#     
# for i in range(nr):
#     print("Rodada ", i+1)
#     for j in dic:
#         time = int(input(f'''Resultado da partida para {j}
#             1 - Vitória
#             2 - Derrota
#             3 - Empate
#             '''))
#         Pontos(time, j)
# 
# print(f"O time com maior pontuação foi o {max(dic, key=dic.get)} com {dic[max(dic, key=dic.get)]}")
# =============================================================================

# =============================================================================
# # Exercício 3
# try:
#     print(sum(list(map(int,(list(str(int(input("Insira um número maior que zero\n")))))))))
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
# senha = input("Insira a senha: ")
# senhabin=[]
# binario = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001"]
# for i in list(senha):
#     if 97<= ord(i) and ord(i) <=122:
#         senhabin.append(list(str(ord(i)-97)))
#     elif i.isdigit():
#         senhabin.append(i)
#     else:
#         senhabin.append("0")
# 
# binzin = []
# for lista in senhabin:
#     for item in lista:
#         binzin.append(item)
#         
# cod = ""
# for i in binzin:
#     cod += binario[int(i)] + "_"
#     
# print(cod[:-1])
# =============================================================================
    
# =============================================================================
# # Exercício 7
# lista=[]
# menu = int(input("""1 - Adicionar
# 2 - Conferir a média de um aluno
# """))
# if menu == 1:
#     qnt = int(input("Insira a quantidade de alunos que pretende colocar: "))
#     arquivo = open("arquivo.txt", "a")
#     for i in range(qnt):
#         arquivo.write(input("Coloque o nome do aluno: "))
#         arquivo.write("\n")
#         arquivo.write(input("Insira a nota 1: "))
#         arquivo.write("\n")
#         arquivo.write(input("Insira a nota 2: "))
#         arquivo.write("\n")
#     arquivo.close()
# else:
#     arquivo = open("arquivo.txt", "r")
#     for linha in arquivo:
#         lista.append(linha.rstrip('\n'))
#     print("Os alunos são: ")
#     for i in range(0, len(lista), 3): 
#         print(lista[i], "\n")
#     nome = input("Selecione um aluno: \n")
#     ind = lista.index(nome)
#     print(f"A média do {nome} é {(float(lista[ind+1]) + float(lista[ind+2]))/2}")
# =============================================================================
    
# =============================================================================
# # Exercício 8
# import pandas as pd
# import matplotlib.pyplot as plt
# 
# netflix = pd.read_csv("netflix_titles.csv", sep=',')
# netflix.info()
# netflix = netflix.dropna()
# 
# 
# netflixbr = netflix[(netflix["country"] == "Brazil")]
# netflixbr = netflixbr[netflixbr["duration"].str.contains("min")]
# netflixbr = netflixbr.reset_index()
# netflixbr["duration"]= netflixbr["duration"].str.replace(" min", "")
# netflixbr['duration']= netflixbr['duration'].astype(int)
# netflixbr = netflixbr.sort_values(by='duration', ascending=False)
# netflixbr = netflixbr.head(5)
# 
# 
# netflix = netflix[((netflix["country"] == "United States") & ((netflix["release_year"]==2015) | (netflix["release_year"]==2016) | (netflix["release_year"]==2017) | (netflix["release_year"]==2018) | (netflix["release_year"]==2019) | (netflix["release_year"]==2020)))]
#         
# a2015 = netflix.release_year[netflix["release_year"] == 2015].count()
# a2016 = netflix.release_year[netflix["release_year"] == 2016].count()
# a2017 = netflix.release_year[netflix["release_year"] == 2017].count()
# a2018 = netflix.release_year[netflix["release_year"] == 2018].count()
# a2019 = netflix.release_year[netflix["release_year"] == 2019].count()
# a2020 = netflix.release_year[netflix["release_year"] == 2020].count()
# 
# plt.bar(("2015", "2016", "2017", "2018", "2019", "2020"), (a2015,a2016,a2017,a2018,a2019,a2020))
# =============================================================================

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
