# =============================================================================
# # Exercício 1 - Verificar se ponto está dentro do poligono
# 
# poligono = [(10, 10), (5, 8), (3, 5), (5, 0), (11, 1), (14, 6)]
# 
# 
# pontos = [(5, 5), (15, 10)]
# 
# # a = poligono[0]
# # b = poligono[1]
# # p = pontos[0]
# 
# 
# for i in range(0, len(poligono)):
#     a = poligono[i]
#     if i + 1 >= len(poligono):
#         b = poligono[0]
#     else:
#         b = poligono[i + 1]
#     
#     p = pontos[0]
#     result = ((p[1] - a[1]) * (b[0] - a[0])) - ((p[0] - a[0]) * (b[1] - a[1])) 
#     
#     if result >= 0:
#         print("Está dentro")
#     else:
#         print("Está fora")
#         break
# =============================================================================

# Exercício 2 - Quando numero da lista for igual ao index
