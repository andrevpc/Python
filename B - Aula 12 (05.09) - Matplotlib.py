# =============================================================================
# # Aula sobre Matplotlib
# =============================================================================
# =============================================================================
# # Se colocar help(plt.plot) no console, aparece cada variavel e como usá-la
# =============================================================================

# =============================================================================
# # Teste gráfico de linhas
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('respiradores.csv')
# plt.plot(df.MES,df["AMAZONAS"],marker='o', label = 'Amazonas')
# plt.plot(df.MES,df["ACRE"],marker='o', label = 'Acre')
# plt.plot(df.MES,df["RONDONIA"],marker='o', label = 'Rondônia')
# plt.plot(df.MES,df["RORAIMA"],marker='o', label = 'Roraima')
# plt.plot(df.MES,df["AMAPA"],marker='o', label = 'Amapá')
# plt.plot(df.MES,df["PARA"],marker='o', label = 'Pará')
# plt.plot(df.MES,df["TOCANTINS"],marker='o', label = 'Rondônia')
# plt.legend()
# plt.xticks(rotation='45')
# plt.grid(linestyle='dashed')
# plt.title("Norte")
# plt.show()
# =============================================================================

# =============================================================================
# # # Exercício 1 - Fazer graficos de cada região (Sul, Norte...) por mês e o total
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('respiradores.csv')

# estados_norte = (df.loc[:,['AMAZONAS','ACRE','RONDONIA','RORAIMA','AMAPA','PARA','TOCANTINS']]).sum(axis=1)
# print(estados_norte)
# estados_nordeste = (df.loc[:,['MARANHÃO','PIAUI','RIO GRANDE DO NORTE','CEARA','PARAIBA','BAHIA','PERNAMBUCO','ALAGOAS','SERGIPE']]).sum(axis=1)
# print(estados_nordeste)
# estados_co = (df.loc[:,['GOIAS','MATO GROSSO','MATO GROSSO DO SUL','DISTRITO FEDERAL']]).sum(axis=1)
# print(estados_co)
# estados_sudeste = (df.loc[:,['MINAS GERAIS','ESPIRITO SANTO','RIO DE JANEIRO','SÃO PAULO']]).sum(axis=1)
# print(estados_sudeste)
# estados_sul = (df.loc[:,['PARANA','SANTA CATARINA','RIO GRANDE DO SUL']]).sum(axis=1)
# print(estados_sul)
# plt.plot(df.MES,estados_norte,marker='o', label = 'Norte')
# plt.plot(df.MES,estados_nordeste,marker='o', label = 'Nordeste')
# plt.plot(df.MES,estados_co,marker='o', label = 'Centro-Oeste')
# plt.plot(df.MES,estados_sudeste,marker='o', label = 'Sudeste')
# plt.plot(df.MES,estados_sul,marker='o', label = 'Sul')
# plt.plot(df.MES,df['TOTAL'],marker='o', label = 'Total')
# plt.plot(df.MES,df.TOTAL/5,marker='o', label = 'Média')
# plt.legend()
# plt.xticks(rotation='45')
# plt.grid(linestyle='dashed')
# plt.show()
# =============================================================================
