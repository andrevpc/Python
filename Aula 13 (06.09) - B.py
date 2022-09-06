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
# 
# numeros = np.random.rand(20) * 20
# print(numeros)
# 
# plt.plot(numeros)
# plt.xticks(rotation='45')
# plt.grid(linestyle='dashed')
# plt.show()
# =============================================================================

# =============================================================================
# # Exercício 4 - 

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

# Exercício 2 - Quantidades de pessoas por quantidade de parentes a bordo e
# quantidade por idade, diferenciandopor sexo
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
titanic = pd.read_csv('titanic.csv')

titanic["Relatives"] = titanic["SibSp"] + titanic["Parch"]
passageiros_parente = titanic.groupby("Relatives")["PassengerId"].count()
passageiros_filho = titanic.groupby("SibSp")["PassengerId"].count()
passageiros_irmao = titanic.groupby("Parch")["PassengerId"].count()
print(passageiros_parente)

plt.plot(titanic["Relatives"].count(),marker='o', label = 'Parentes')
plt.plot(titanic["SibSp"].count(),marker='o', label = 'Irmão')
plt.plot(titanic["Parch"].count(),marker='o', label = 'Pai')
plt.legend()
plt.xticks(rotation='45')
plt.grid(linestyle='dashed')
plt.show()