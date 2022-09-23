# text to ascii

# =============================================================================
# # Desafio 1 - jogo de anagrama
# import random
# 
# defs = ["l3.txt","l4.txt","l5.txt","l6.txt","l7.txt","l8.txt","l9.txt"]
# 
# def escolha(dificuldade):
#     lista = []
#     with open(defs[dificuldade-3]) as arquivo:
#         for linha in arquivo:
#             palavras = linha.strip().split()
#             lista.append(palavras[0])
#     n = random.randint(0,4)
#     palavra_normal = (lista[n])
#     anagrama = list(palavra_normal)
#     random.shuffle(anagrama)
#     anagrama = ''.join(anagrama)
#     return [palavra_normal,anagrama]
# 
# print("Jogo dos anagramas!")
# 
# pontos = 100
# 
# while 1:
#     if pontos < 0:
#         print("Seus pontos acabaram, você perdeu!")
#         break
#     elif pontos > 200:
#         print("Você ganhou")
#     
#     dificuldade = int(input("""
# 3 para 3 letras
# 4 para 4 letras
# 5 para 5 letras
# 6 para 6 letras
# 7 para 7 letras
# 8 para 8 letras
# 9 para 9 letras
# Escolha a dificuldade: """))   
#                     
#     if dificuldade == 3:
#         adicional = 30
#         palavras = escolha(3)
#         palavra_normal = palavras[0]
#         anagrama = palavras[1]
#         
#     elif dificuldade == 4:
#         adicional = 40
#         palavras = escolha(4)
#         palavra_normal = palavras[0]
#         anagrama = palavras[1]
#     
#     elif dificuldade == 5:
#         adicional = 50
#         palavras = escolha(5)
#         palavra_normal = palavras[0]
#         anagrama = palavras[1]
#         
#     elif dificuldade == 6:
#         adicional = 60
#         palavras = escolha(6)
#         palavra_normal = palavras[0]
#         anagrama = palavras[1]
#         
#     elif dificuldade == 7:
#         adicional = 70
#         palavras = escolha(7)
#         palavra_normal = palavras[0]
#         anagrama = palavras[1]
# 
#     elif dificuldade == 8:
#         adicional = 80
#         palavras = escolha(8)
#         palavra_normal = palavras[0]
#         anagrama = palavras[1]
# 
#     elif dificuldade == 9:
#         adicional = 90
#         palavras = escolha(9)
#         palavra_normal = palavras[0]
#         anagrama = palavras[1]
#         
#     print("Você escolheu",dificuldade,"letras")        
#         
#     while 1:
#             print(anagrama)
#             resposta = input("Descubra a palavra: ")
#             if resposta == palavra_normal:
#                 pontos += adicional
#                 print(f'''Você ganhou {adicional} pontos
# Agora sua pontuação é:''', pontos)     
#                 print("Você acertou!")
#                 break
#             else:
#                 pontos -= adicional
#                 print(f'''Você perdeu {adicional} pontos
# Agora sua pontuação é:''', pontos) 
#                 print("Você errou, tente novamente") 
#                 if pontos <= 0:
#                     print("A resposta era: ", palavra_normal)
#                     break
# =============================================================================

# Desafio 2 - lig - 4 

def tabuleiro(j):
    print("          Jogador x" if j == "o" else "          Jogador o")
    print('  1  ','2  ','3  ','4  ','5  ','6  ','7')
    for i in linhas:
        for j in i:
            print('| ',j,end='')
        print("|")

def jogada(jogador):    
    x = int(input("Escolha a coluna: "))
    if linhas[0][x-1] == " ":
        for i in range(5,-1,-1):                
            if linhas[i][x-1] == ' ':
                linhas[i][x-1] = jogador
                break
    else:
        print("Coluna já preenchido! Escolha outra")
        jogada(jogador)
        
def vitoria():
    for i in linhas:
        for j in range(4):
            if i[j+0] == i[j+1] == i[j+2] == i[j+3] != " ":
                return 1  

    for j in range(7):
        for i in range(3):
            if linhas[i][j] == linhas[i+1][j] == linhas[i+2][j] == linhas[i+3][j] != " ":
                return 1

    for j in range(4):
        for i in range(3):
            if linhas[i][j] == linhas[i+1][j+1] == linhas[i+2][j+2] == linhas[i+3][j+3] != " ":
                return 1
        
    for j in range(4):
        for i in range(3):
            if linhas[5-i][j] == linhas[4-i][j+1] == linhas[3-i][j+2] == linhas[2-i][j+3] != " ":
                return 1
            
print('''
      _               _     
 ___/__) ,           /   / 
(, /        _   __  /___/_ 
  /    _(_ (_/_        /   
 (_____   .-/         /    
         (_/               ''')
        
lin1= [' ',' ',' ',' ',' ',' ',' ']
lin2= [' ',' ',' ',' ',' ',' ',' ']
lin3= [' ',' ',' ',' ',' ',' ',' ']
lin4= [' ',' ',' ',' ',' ',' ',' ']
lin5= [' ',' ',' ',' ',' ',' ',' ']
lin6= [' ',' ',' ',' ',' ',' ',' ']

linhas = [lin1,lin2,lin3,lin4,lin5,lin6]
j = "x"

tabuleiro(j)

while 1:
    if j == "o":
        j="x"
    else:
        j="o"
    
    jogada(j)
    tabuleiro(j)
    if vitoria() == 1:
        print("Jogador x ganhou" if (j=="x") else "Jogador o ganhou")
        break
