# =============================================================================
# # Exercício 1
# def divisoes(lt,l1,l2,l3):
#     for i in lt:
#         separada = (list(str(i)))
#         nomeseparado = separada[2:]
#         if separada[0] == "1":
#             l1.append("".join(nomeseparado))
#         if separada[0] == "2":
#             l2.append("".join(nomeseparado))
#         if separada[0] == "3":
#             l3.append("".join(nomeseparado))
#     print('Primeira divisão: ', l1)
#     print('Segunda divisão: ', l2)
#     print('Terceira divisão: ', l3)
#         
# listatotal = ["1_palmeiras", "2_coritiba", "1_corinthians", "3_juventude", "2_fluminense", "3_bahia", "1_cuiaba", "2_cascavel", "3_ponte preta", "2_parana clube", "3_voltaredonda"]
# lista1 = []
# lista2 = []
# lista3 = []
# divisoes(listatotal, lista1, lista2, lista3)
# =============================================================================

# =============================================================================
# # Exercício 2
# import numpy as np
# 
# array = np.random.randint(0,10,25)
# 
# print('A array original:\n', array.reshape(5,5))
# soma = 0
# 
# for i in range(len(array)):
#     if array[i]%2 != 0:
#         soma += 1
#         
# arquivo = open("arq.txt", "a")
# arquivo.write(f"{soma}\n")  
# arquivo.close()
# 
# array[array%2 != 0] = array[array%2 != 0]**2
# 
# arquivo = open("arq.txt", "r")
# print("\nA array substituindo os números ímpares: \n", array.reshape(5,5))
# print(f"Existem {len(arquivo.readlines())} registros.")
# arquivo.close()
# =============================================================================

# =============================================================================
# # Exercício 3
# import numpy as np
# 
# def palindromo(frases):
#     for i in range(frases):
#         teste = (input(f"Insira a {i+1}° frase\n"))
#         testemin = (list(teste.lower().replace(" ","")))
#         if testemin == testemin[::-1]:
#             frasespalin.append(teste)
# 
# frases = int(input("Quantas frases deseja verificar? "))
# frasespalin = []
# palindromo(frases)
# print("\nSão palindromos:\n")
# for i in frasespalin:
#     print(i)
# =============================================================================

# =============================================================================
# # Exercício 4
# def notas(*lista,sit = False):
#     total = len(lista)
#     maior = max(lista)
#     menor = min(lista)
#     media = round((sum(lista)/total),2)
#     if sit == True:
#         return {"total": total, "maior": maior, "menor": menor, "média": media, "situacao": ("Boa" if media>7 else("Razoável" if 5<media<7 else "Ruim"))}
# 
#     return {"total": total, "maior": maior, "menor": menor, "média": media}
# 
# print(notas(5.5,2.5,1.5))
# print(notas(5.5,2.5,9.9, sit=True))
# =============================================================================

# =============================================================================
# # Exercício 5
# # 1, 5, 10, 50 e 100
# def caixa(v):
#     if 10<=v<=600:
#         n100 = v/100
#         v = v - int(n100)*100
#         n50 = v/50
#         v = v - int(n50)*50
#         n10 = v/10
#         v = v - int(n10)*10
#         n5 = v/5
#         v = v - int(n5)*5
#         n1 = v/1
#         v = v - int(n1)
#         print("Notas para saque:")
#         print("1 nota de R$100,00") if int(n100) == 1 else (print(f"{int(n100)} notas de R$100,00") if int(n100)>1 else "")
#         print("1 nota de R$50,00") if int(n50) == 1 else (print(f"{int(n50)} notas de R$50,00") if int(n50)>1 else "")
#         print("1 nota de R$10,00") if int(n10) == 1 else (print(f"{int(n10)} notas de R$10,00") if int(n10)>1 else "")
#         print("1 nota de R$5,00") if int(n5) == 1 else (print(f"{int(n5)} notas de R$5,00") if int(n5)>1 else "")
#         print("1 nota de R$1,00") if int(n1) == 1 else (print(f"{int(n1)} notas de R$1,00") if int(n1)>1 else "")
#     else:
#         print("Valor inválido")
#         caixa(int(input("Novo valor: ")))
#  
# caixa(int(input("Insira qual valor deseja sacar: (minímo R$10,00)\n")))
# =============================================================================

# =============================================================================
# # Exercício 6
# import pandas as pd
# import matplotlib.pyplot as plt
# 
# sh = pd.read_csv("superheroes.csv", sep=',')
# sh = sh.dropna()
# forca = sh.groupby("creator")["strength_score"].mean()
# forca = forca.reset_index()
# 
# plt.bar(forca["creator"], forca["strength_score"], color="k", zorder=2)
# plt.xticks(rotation=45)
# plt.ylabel("Strengh mean")
# plt.grid(linestyle='-')
# 
# imortais = sh.loc[sh["has_immortality"] == 1]
# imortais = imortais.sort_values(by = "combat_score", ascending=False)
# imortais = imortais.head(5)
# imortais = imortais.reset_index()
# print("Os melhores imortais em combate são:")
# for i in range(5):
#     print(1+i,"  -  ", imortais['name'][i])
# =============================================================================

# Exercício 7
import random

listausp = []
with open("bancodepalavras.txt") as arquivo:
    for linha in arquivo:
        palavras = linha.strip().split()
        listausp.append(palavras[0])
n = random.randint(0,245365)
palavra = (listausp[n])
listapalavra = list(str(palavra))
placar = 6
chute = ""
listachutes = []
listacertas = []

for i in range(len(listapalavra)):
    listacertas.append("_")

while 1:
    try:
        if placar == 0:
            raise Exception()
            
        for i in range(len(listapalavra)):
            print(f"{listacertas[i]}",end=".")
        
        chute = input("Insira uma letra: ")
        
        for i in range(len(listapalavra)):
            if chute == listapalavra[i]:
                listacertas[i] = chute
        if chute in listachutes:
            print("\nLetra já usada, insira outra\n")
        else:
            listachutes.append(chute)
            if chute in listapalavra:
                print(f"\nAcertou, '{chute}' está na palavra\nLetras usadas: {listachutes}\n\nVocê tem {placar} vidas")
            else:
                placar -= 1
                print(f"\nErrou, a letra não está na palavra\nLetras usadas: {listachutes}\n\nVocê tem {placar} vidas")
            if listacertas == listapalavra:
                print(f"{palavra}\nVocê ganhou!")
                break
    except:
        print('Você usou todas as suas tentativas!')
        print(f'A palavra era {palavra}')
        print("Você perdeu")
        break