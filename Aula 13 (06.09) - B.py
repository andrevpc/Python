# Se colocar help(plt.plot) no console, aparece cada variavel e como usá-la

# =============================================================================
# # Lista 1
# =============================================================================

# =============================================================================
# # Exercício 1 - Fazer graficos do sen, cos e tg num intervalo de -3 até 3
# # com 100 números
# import numpy as np
# import matplotlib.pyplot as plt
# 
# numeros = np.linspace(-3,3,100)
# print(numeros)
# 
# fig, eixo = plt.subplots(nrows = 2, ncols = 2, figsize = (20,20))
# eixo[0][0].plot(np.sin(numeros), color = 'red', label = "Seno")
# eixo[0][0].legend()
# eixo[0][0].set_title("Seno")
# eixo[0][1].plot(np.cos(numeros), color = 'blue', label = "Cosseno")
# eixo[0][1].legend()
# eixo[0][1].set_title("Cosseno")
# eixo[1][0].plot(np.tan(numeros), color = 'purple', label = "Tangente")
# eixo[1][0].legend()
# eixo[1][0].set_title("Tangente")
# =============================================================================

# =============================================================================
# # Exercício 2 - Gráfico de pizza com número de habitantes de 6 cidades
# import matplotlib.pyplot as plt
# 
# estados = ["Araucária", "Campo Largo", "Colombo", "Fazenda Rio Grande", "Pinhais", "São José dos Pinhais"]
# val = [141410, 130091, 240840, 98368, 130789, 317476]
# 
# p, tx, autotexts = plt.pie(val, labels=estados, 
#         autopct="", shadow=True)
# for i, a in enumerate(autotexts):
#     a.set_text(val[i])
# =============================================================================

# =============================================================================
# # Exercício 3 - Gráfico com pontos randômicos de 0<=x<=20 e fazer uma linha
# # na média total azul, uma na media + desvio padrao azul e traço-traço, uma na
# # media - desvio padrao azul e traço-traço
# import numpy as np
# import matplotlib.pyplot as plt
# y = np.random.rand(100)
# x= np.linspace(0,20,100)
# plt.plot(x,y, color = 'k')
# plt.plot([np.mean(y)]*21, color = 'b')
# plt.plot([np.mean(y)+np.std(y)]*21, color = 'b', linestyle = '--')
# plt.plot([np.mean(y)-np.std(y)]*21, color = 'b', linestyle = '--')
# plt.grid(linestyle='dashed')
# plt.show()
# =============================================================================

# =============================================================================
# # Exercício 4 - Usar linha de meses e temp media max e min para fazer um gráfico
# # preenchido
# import matplotlib.pyplot as plt
# meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
# temp_max = [26.8, 26.8, 26, 24, 20.8, 20.1, 19.7, 21.5, 21.4, 23.1, 25, 26.2]
# temp_min = [17.2, 17.4, 16.5, 14.6, 11.2, 9.7, 9, 9.6, 11.1, 13.2, 14.9, 16.2]
# fig,ax1 = plt.subplots(figsize=(10,4))
# ax1.plot(meses, temp_max, marker = "o", color = 'r', label = "Temperatura Máxima")
# ax1.plot(meses, temp_min, marker = "o", color = 'b', label = "Temperatura mínima")
# plt.fill_between(meses, temp_max, temp_min, color = "indianred")
# plt.fill_between(meses, temp_min, color = "royalblue")
# plt.yticks([0, 15, 30])
# plt.axis([0,11,0,30])
# plt.xlabel("Meses")
# plt.ylabel("Temperatura")
# plt.grid(True, linewidth=1, linestyle='-')
# =============================================================================

# =============================================================================

# =============================================================================
# # Lista 2
# =============================================================================

# =============================================================================
# # Exercício 1 - Gráficos do titanic com pessoas sobrevivente e não
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('titanic.csv')
#         
# vivo = df.Survived[df["Survived"] == 1].count()
# morto = df.Survived[df["Survived"] == 0].count()
# 
# 
# plt.bar(("Vivos", "Mortos"), (vivo,morto))
# =============================================================================

# =============================================================================
# # Exercício 2 - Quantidades de pessoas por quantidade de parentes a bordo
# import pandas as pd
# import matplotlib.pyplot as plt
# titanic = pd.read_csv('titanic.csv')
# 
# titanic["Relatives"] = titanic["SibSp"] + titanic["Parch"]
# passageiros_parente = titanic.groupby("Relatives")["PassengerId"].count()
# passageiros_irmao = titanic.groupby("SibSp")["PassengerId"].count()
# passageiros_filho = titanic.groupby("Parch")["PassengerId"].count()
# print(passageiros_parente)
# 
# plt.plot(passageiros_parente,marker='o', label = 'Parentes')
# plt.plot(passageiros_irmao,marker='o', label = 'Irmão')
# plt.plot(passageiros_filho, marker='o', label = 'Filhos')
# plt.legend()
# plt.xlabel("Quantidade de parentes")
# plt.ylabel("Quantidade de pessoas")
# plt.grid(linestyle='-')
# plt.show()
# =============================================================================

# Exercício 3 - Quantidade de pessoas por idade, diferenciando por sexo
import pandas as pd
import matplotlib.pyplot as plt
titanic = pd.read_csv('titanic.csv')
x = titanic.groupby("Age")["PassengerId"].count()
y = titanic.Age.count
print(y)
plt.plot(x)