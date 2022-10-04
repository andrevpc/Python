# =============================================================================
# # Exercício 2 - Pegar dados estatisticos de duas colunas (Age e Pclass)
# import pandas as pd
# 
# titanic = pd.read_csv("titanic.csv", sep=',')
# print(titanic.loc[:,["Age", "Pclass"]].describe())
# =============================================================================

# =============================================================================
# # Exercício 3 - Pegar as colunas "crim" e "medv" e mostrar as primeira
# # 14 linhas
# import pandas as pd
# 
# boston = pd.read_csv("BostonHousing.csv", sep=',')
# print(boston.loc[:13,["crim", "medv"]])
# =============================================================================

# =============================================================================
# # Exercício 4 - Filtrar carros por 5 passageiros, 10 com mais MPG, 5 mais
# # baratos e mostrar somente as colunas 'Manufacturer','Make','Price',
# # 'MPG.city','Type','Passengers'
# import pandas as pd
# 
# carro = pd.read_csv("Cars93_miss.csv", sep=',')
# carro = carro[carro["Passengers"]==5]
# carro = carro.sort_values(by = "MPG.city",ascending=False).head(10)
# carro = carro.sort_values(by = "Price",ascending=True).head(5)
# print(carro[['Manufacturer','Make','Price','MPG.city','Type','Passengers']])
# =============================================================================

# =============================================================================
# # Exercício 5 - Filtrar por 1° classe que sobreviveu e 3° classe que morreu
# import pandas as pd
# 
# titanic = pd.read_csv("titanic.csv", sep=',')
# titanic = titanic[((titanic["Pclass"] == 1) & (titanic["Survived"] == 1)) | ((titanic["Pclass"]==3) & (titanic["Survived"]==0))]
# print(titanic)
# =============================================================================

# =============================================================================
# # Exercício 6 - Encontre a mulher que Robin se apaixonou, embarcou em
# # Southhampton, segunda classe, 29 anos, tem Anne no nome. Retire os NaN e 
# # coloque outros valores
# import pandas as pd
# 
# titanic = pd.read_csv("titanic.csv", sep=',')
# titanic = titanic[titanic["Embarked"]=="S"]
# titanic = titanic[titanic["Pclass"]==2]
# titanic = titanic[titanic["Age"]==29]
# titanic = titanic[titanic["Name"].str.contains("Anne")]
# titanic = titanic.fillna("0")
# mulher = titanic.to_string(columns = ["Name"],index=False,header=False)
# sobrevivente = titanic.to_string(columns = ["Survived"],index=False,header=False)
# print(f"A mulher se chama {mulher} e está {'Viva' if sobrevivente == ' 1' else 'Morto'}")
# =============================================================================
